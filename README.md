# Scrapper So Foot League
Pour récupérer les informations sur les matches et votre team

## Récupérer les matches (Compétitions, équipes & cotes)
```
python3 scrapMatches.py -e <Votre e-mail> -p <Votre Password> -d <La date demandée>
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
python3 scrapTeamPicks.py -e <Votre e-mail> -p <Votre Password>
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
python3 scrapTeamResults.py -e <Votre e-mail> -p <Votre Password>
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


## Envoyer ces informations sur Slack
```
python3 sendMatchesToSlack.py
python3 sendResultsToSlack.py
python3 sendPickssToSlack.py
```

Les 3 classes ``sendXXXToSlack`` permettent d'envoyer les éléments scrappés dans Slack (automatiquement dans le channel sfl), avec un formattage adapté. 

Exemple: 
```
En *Coupe de France* :
 Lens _(1.53)_ vs Boulogne _(7.00)_

En *FA Cup* :
 B & H Albion _(2.62)_ vs Crystal Palace _(3.00)_

En *Liga* :
 Malaga _(2.60)_ vs Espanyol _(2.90)_

En *Portugal Primeira Liga* :
 Paços Ferreira _(2.38)_ vs Portimonense _(3.00)_
 Estoril-Praia _(1.85)_ vs CD Feirense _(4.50)_
```

Pour que ces scripts fonctionnent, il faut que soient passés en variable d'environnment du système : 

``sfl_email`` : Votre email

``sfl_password`` : Votre mot de passe

``sfl_slackwebhook`` : Le lien vers le [webhook Slack](https://api.slack.com/incoming-webhooks)

