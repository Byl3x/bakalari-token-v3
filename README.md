# Bakalari token generator v3
Generator tokenu pro bakalare, pro v3 verzi API napsany v pythonu.  
Refresh token je ted implementovan 
# Usage
importujte modul, pouzijte:  `gettoken.getAccessToken(<url serveru>, <username>, <heslo>)` nebo  
`gettoken.getLoginToken(<url serveru>, <access token>)`  
nebo `gettoken.refreshToken(<url serveru>, <refrshtoken>)`  
`getAccessToken` vraci tuple kde na pozici 0 je accessToken a na pozici 1 je refreshToken  
`getLoginToken` vraci string
`refreshToken` vraci tuple kde na pozici 0 je accessToken a na pozici 1 je refreshToken  
Platnost accessTokenu je 600 sekund  
Platnost loginTokenu a refreshTokenu je 1 vuyziti
