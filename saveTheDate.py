from datetime import datetime

# Ottieni la data e l'ora correnti
now = datetime.now()

# Formatta la data e l'ora
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Scrivi la data e l'ora in un file su una nuova riga
with open('dataora.txt', 'a') as file:
    file.write(formatted_time + '\n')  # Aggiungi una nuova riga

# Stampa la data e l'ora nel terminale
print(f"Data e ora salvate: {formatted_time}")
