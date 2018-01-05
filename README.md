# Scrapper So Foot League
Pour récupérer les informations sur les matches et votre team

## Récupérer les matches (Compétitions, équipes & cotes)
```
scrapMatches.py -e <Votre e-mail> -p <Votre Password> -d <La date demandée>
```

L'argument date est optionnel, par défaut cela récupérera les matches du jour même

Retour en CSV : competition,equipe1,cote1,equipe2,cote2

Exemple : 
```
FA Cup,Liverpool,1.40,Everton,9.00
FA Cup,Manch. Utd,1.25,Derby County,16.00
Serie A,Chievo,3.00,Udinese,2.50
Serie A,Fiorentina AC,2.75,Inter Milan,2.70
```