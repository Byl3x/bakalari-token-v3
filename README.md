# Bakalari token generator v3
Generator tokenu pro bakalare, pro v3 verzi API napsany v pythonu.  
Refresh token implementace jeste neni, vzdy je potreba heslo.  
# Usage
importujte modul, pouzijte:  `gettoken.getAccessToken(<url serveru>, <username>, <heslo>)` nebo  
`gettoken.getLoginToken(<url serveru>, <access token>)`
obe funkce vraci string.
