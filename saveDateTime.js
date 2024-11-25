const fs = require('fs');
const path = require('path');

// Ottieni la data e l'ora correnti
const now = new Date();
const formattedDate = now.toISOString().replace('T', ' ').substring(0, 19);

// Percorso del file
const filePath = path.join(__dirname, 'dataoraNode.txt');

// Scrivi la data e l'ora nel file
fs.appendFile(filePath, formattedDate + '\n', (err) => {
    if (err) {
        console.error('Errore durante il salvataggio:', err);
    } else {
        console.log(`Data e ora salvate: ${formattedDate}`);
    }
});
