import smtplib

server = smtplib.SMTP_SSL("smtp.sendgrid.net", 465)
server.login("apikey", "SUA_API_KEY_REAL")
server.sendmail(
    "testedjango11@gmail.com", 
    "masternoob500@gmail.com", 
    "Subject: Teste\n\nEmail funcionando"
)
server.quit()

print("ENVIADO")