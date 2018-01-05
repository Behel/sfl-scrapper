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


## Récupérer les picks de l'équipe
```
scrapTeamPicks.py -e <Votre e-mail> -p <Votre Password>
```

Retour en CSV : user,pick

Exemple : 
```
azerty774,Estoril-Praia
Benjbenj (admin),Tottenham
Chupito,Tottenham
sjankowski,Estoril-Praia
Wahoc,Vitoria
Etien,Estoril-Praia
Bessao,Tottenham
Izecson,
```



## Récupérer les résultats de l'équipe
```
scrapTeamResults.py -e <Votre e-mail> -p <Votre Password>
```

Retour en CSV : user,previousPick,points

Exemple : 
```
azerty774,Estoril-Praia,23
Benjbenj (admin),Tottenham,11
Chupito,Tottenham,11
sjankowski,Estoril-Praia,23
Wahoc,Vitoria,24
Etien,Estoril-Praia,23
Bessao,Tottenham,11
Izecson,,0
```