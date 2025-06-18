import pandas as pd
import streamlit as st

# Titre de l'application
st.title("📊 Visualisation des ventes - Kéfir Project")

# Lire le fichier CSV
csv_path = "data/sales_data.csv"

try:
    df = pd.read_csv(csv_path)
    df['order_date'] = pd.to_datetime(df['order_date'])

    # 🔍 Diagnostique des données
st.write("🔍 Colonnes du DataFrame :", df.columns.tolist())
st.write("🔍 Quelques lignes :", df.head())
st.write("🔍 Types de colonnes :", df.dtypes)


    # Afficher les données
    st.subheader("🗂️ Données brutes")
    st.dataframe(df)

    # Résumé par client
    st.subheader("📈 Total dépensé par client")
    summary = df.groupby("customer_name")["amount"].sum().reset_index()
    summary.columns = ["Client", "Total (€)"]
    st.dataframe(summary)

    # Graphique en barres
    st.subheader("📊 Visualisation graphique")
    st.bar_chart(data=summary.set_index("Client"))

except FileNotFoundError:
    st.error(f"Fichier CSV non trouvé à l'emplacement : `{csv_path}`")

# 📥 Télécharger le PDF généré (s'il existe)
import os

st.subheader("📄 Télécharger le rapport PDF")

pdf_folder = "."
pdf_files = sorted(
    [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")],
    key=lambda x: os.path.getmtime(os.path.join(pdf_folder, x)),
    reverse=True
)

if pdf_files:
    latest_pdf = pdf_files[0]
    with open(latest_pdf, "rb") as f:
        st.download_button(
            label=f"📥 Télécharger {latest_pdf}",
            data=f.read(),
            file_name=latest_pdf,
            mime="application/pdf"
        )
else:
    st.info("Aucun fichier PDF trouvé pour le moment.")
