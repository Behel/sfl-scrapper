import slackweb, os
import scrapLigueEuropa

##############################
# Récupération des arguments #
##############################

email = os.getenv('sfl_email')
password = os.getenv('sfl_password')
team_name = "Brazilala"
slackWebhook = os.getenv('sfl_slackwebhook')

csvResults = scrapLigueEuropa.main(email, password, team_name)
resultats = ''
slack = slackweb.Slack(url=slackWebhook)
lines = csvResults.split('\n')
team1 = lines[0].split(',')[0]
points1 = lines[0].split(',')[1]
team2 = lines[1].split(',')[0]
points2 = lines[1].split(',')[1]

if points2 < points1:
    resultats += "*" + team1 + "* est devant *" + team2 + "* par " + points2-points1 + " points d'avance ! _(" + \
                 points1 + " pts vs " + points2 + " pts)_"
elif points2 > points1:
    resultats += "*" + team2 + "* est devant *" + team1 + "* par " + points1 - points2 + " points d'avance ! _(" + \
                 points2 + " pts vs " + points1 + " pts)_"
else:
    resultats += "*" + team1 + "* et *" + team2 + "* sont à égalité ! " + points2 + " pts chacun !"

print(resultats)
slack.notify(
                text=resultats,
                icon_url="http://azerty774.free.fr/sfl_cup.png",
                username="La confrontation Europa Ligue",
                channel="@sfl"
             )
