import slackweb, os
import scrapCoupe

##############################
# Récupération des arguments #
##############################

email = os.getenv('sfl_email')
password = os.getenv('sfl_password')
slackWebhook = os.getenv('sfl_slackwebhook')

csvResults = scrapCoupe.main(email, password)
resultats = ''
slack = slackweb.Slack(url=slackWebhook)
lines = csvResults.split('\n')
for line in lines:
    if line != "" :
        elements = line.split(',')
        place = elements[0]
        team = elements[1]
        points = elements[2]
        if place == "1":
            resultats+= team + " *est qualifiée* et en *1re place* avec " + points + " pts\n"
        elif place == "2":
            resultats+= team + " *est qualifiée* et en *2nde place* avec " + points + " pts\n"
        else :
            resultats+= team + " _est lamentablement éliminée _ ("+place+"e place) avec seulement " + points + " pts\n"

print(resultats)
slack.notify(
                text=resultats,
                icon_url="http://azerty774.free.fr/sfl_cup.png",
                username="Le classement de la Coupe",
                channel="sfl"
             )
