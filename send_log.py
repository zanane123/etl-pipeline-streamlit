import smtplib
from email.message import EmailMessage

# 📄 Fichier à envoyer
log_file = "etl.log"

# 📧 Infos d'envoi
sender_email = "zananecci@gmail.com"
receiver_email = "zananecci@email.com"
password = "zkpm fdub fyvz mjjq"  # ⚠️ voir plus bas pour l'alternative sécurisée

# 📬 Créer l'e-mail
msg = EmailMessage()
msg["Subject"] = "📊 Log ETL - Résultat du pipeline"
msg["From"] = "zananecci@gmail.com"
msg["To"] = "zananecci@gmail.com"
msg.set_content("Bonjour,\n\nVoici le fichier de log généré par le pipeline ETL.\n\nCordialement,\nTon script Python.")

# 📎 Attacher le fichier .log
with open(log_file, "rb") as f:
    msg.add_attachment(f.read(), maintype="text", subtype="plain", filename=log_file)

# 🔐 Connexion au serveur SMTP
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender_email, password)
    smtp.send_message(msg)

print("✅ E-mail envoyé avec succès.")

