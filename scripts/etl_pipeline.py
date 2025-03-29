import pandas as pd
from sqlalchemy import create_engine, text
import os
import argparse
import logging
# Initialisation du logger
logging.basicConfig(
    filename='etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def main():
    # Lire les arguments (comme --summary)
    parser = argparse.ArgumentParser(description="ETL CSV to SQLite")
    parser.add_argument('--summary', action='store_true', help="Afficher un résumé par client")
    args = parser.parse_args()

    # Chemins
    csv_path = os.path.join('data', 'sales_data.csv')
    db_path = os.path.join('db', 'sales.db')

    # Vérifie que le fichier existe
    if not os.path.exists(csv_path):
        print(f"❌ Fichier introuvable : {csv_path}")
        logging.error(f"Fichier CSV introuvable : {csv_path}")
        return

    # Lire les données
    df = pd.read_csv(csv_path)
    df.columns = [col.strip().lower() for col in df.columns]
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Connexion à la base et insertion
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql("sales", con=engine, if_exists="replace", index=False)
    print("✅ Données chargées dans SQLite.")
    logging.info("Données chargées dans SQLite avec succès.")


    # Si l’option --summary est présente
    if args.summary:
        with engine.connect() as connection:
            result = connection.execute(text("""
                SELECT customer_name, SUM(amount) AS total_spent
                FROM sales
                GROUP BY customer_name
            """))
            print("\n📊 Résumé par client :")
            for row in result:
                print(f"{row.customer_name}: {row.total_spent:.2f} €")
                logging.info(f"{row.customer_name} a dépensé {row.total_spent:.2f} €")

# Exécuter si le script est lancé directement
if __name__ == "__main__":
    main()

