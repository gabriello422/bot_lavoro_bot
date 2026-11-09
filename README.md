# Bot Lavoro — @bot_lavoro_bot

Copia del bot originale, con attivazione tramite codice e senza ID Telegram fisso.

## Railway
1. Carica la cartella del progetto in un repository GitHub.
2. Configura le variabili Railway `BOT_TOKEN` (token Telegram) e `ACTIVATION_CODE` (scegli una password lunga e casuale, privata; non inserirla nel codice o su GitHub).
3. Imposta Start Command `python main.py`.
4. Per la mini app puoi configurare `MINI_APP_URL` con l'URL HTTPS pubblico; altrimenti viene usato `RAILWAY_PUBLIC_DOMAIN`.
5. Su Telegram, invia `/start`, poi `/attiva TUO_CODICE`. Solo il primo utente con codice corretto diventa proprietario.

## Prova e passaggio al nuovo proprietario
- Puoi attivare e provare il bot dal tuo Telegram.
- Per liberare il bot, invia `/trasferisci TUO_CODICE` dal tuo account proprietario.
- Il nuovo utilizzatore invia `/attiva TUO_CODICE` dal suo Telegram.
- **Attenzione:** `/trasferisci` non cancella timbrature o lavori; prima di consegnarlo, esporta i dati e usa `Reset mese` se vuoi svuotare le registrazioni. Il reset elimina i dati registrati, quindi esportali prima.
- Il codice di attivazione è una password: non condividerlo con estranei. Dopo il passaggio, cambialo nelle variabili Railway se vuoi invalidare il precedente.
- Telegram potrebbe conservare il messaggio con il codice se non è possibile eliminarlo automaticamente: puoi cancellarlo manualmente.

## Persistenza
Configura un volume Railway montato su `/data` e le variabili `OWNER_FILE=/data/owner.json` e `DATA_FILE=/data/dati.json` per conservare proprietario e timbrature tra i deploy. Un semplice riavvio NON è un modo affidabile per cambiare proprietario.

Non avviare due istanze polling con lo stesso token.

**Privacy:** la mini app Ore Live conserva l'accesso pubblico dell'originale: chi conosce il link può visualizzarne i dati. Per dati riservati serve autenticazione separata.

## Nome automatico Ore Live
Il nome mostrato proviene dal nome completo Telegram salvato durante `/attiva`. Se il proprietario era già attivo prima di questo aggiornamento, inviare `/start` per aggiornare il nome. La pagina va ricaricata. Il trasferimento cancella anche il nome precedente.
I file statici si trovano in `static/css/style.css` e `static/js/app.js`.


## Nome proprietario su Ore Live
Dopo `/attiva CODICE`, rispondi alla domanda con il nome desiderato.
Per cambiarlo in seguito usa `/cambia_nome Nuovo Nome` oppure `/cambia_nome` e rispondi al messaggio.
La pagina `/ore-live` mostra il nome salvato; in assenza di un nome mostra `Bot Lavoro`.
Il comando `/trasferisci CODICE` elimina anche il nome del precedente proprietario.
