import os
import sqlite3
from scripts.etl_pipeline import main

def test_etl_pipeline():
    # Supprimer la base si elle existe
    db_path = "db/sales.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    # Exécuter le pipeline
    main()

    # Vérifier que la base est bien créée
    assert os.path.exists(db_path), "❌ La base de données n’a pas été créée."

    # Vérifier que la table 'sales' existe
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sales'")
    result = cursor.fetchone()
    conn.close()

    assert result is not None, "❌ La table 'sales' n’a pas été créée."

    print("✅ Test réussi : la base et la table 'sales' existent bien.")

# Lancer le test si ce fichier est exécuté directement
if __name__ == "__main__":
    test_etl_pipeline()
