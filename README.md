# Bot Lavoro — @bot_lavoro_bot

Copia del bot originale con le stesse funzioni e senza ID Telegram fisso.

## Railway
1. Carica questi file in un nuovo repository GitHub (oppure usa Railway con questo progetto).
2. Imposta la variabile `BOT_TOKEN` con il token del nuovo bot (non pubblicarlo su GitHub).
3. Imposta Start Command: `python main.py`.
4. Se disponibile, imposta `MINI_APP_URL` con l’URL pubblico HTTPS del servizio; in alternativa il bot usa `RAILWAY_PUBLIC_DOMAIN`.
5. Avvia il servizio, apri @bot_lavoro_bot su Telegram e invia **/start** prima di chiunque altro.

Il primo account che invia /start diventa proprietario. Gli altri account non possono usare il bot. L’ID viene memorizzato automaticamente in `owner.json` e non va inserito nel codice.

**Importante:** `owner.json` e `dati.json` devono essere conservati su un volume persistente Railway, altrimenti si possono perdere proprietario e timbrature ai riavvii/redeploy. Per esempio, monta un volume su `/data` e configura `OWNER_FILE=/data/owner.json` e `DATA_FILE=/data/dati.json`.

Non avviare contemporaneamente due istanze in polling con lo stesso token.

Il link Ore Live è pubblico, come nel progetto originale: chi conosce l’URL può vedere i dati mostrati nella mini app. Non usarlo per informazioni riservate senza aggiungere autenticazione.
