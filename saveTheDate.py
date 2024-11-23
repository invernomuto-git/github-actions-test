from datetime import datetime

# Ottieni la data e l'ora correnti
now = datetime.now()

# Scrivi la data e l'ora in un file
with open('dataora.txt', 'w') as file:
    file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
