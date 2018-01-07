import slackweb, time, os
import scrapTeamPicks

##############################
# Récupération des arguments #
##############################

email = os.getenv('sfl_email')
password = os.getenv('sfl_password')
requestedDate = time.strftime("%Y-%m-%d")
slackWebhook = os.getenv('sfl_slackwebhook')

csvResults = scrapTeamPicks.main(email, password)
resultats = ''
slack = slackweb.Slack(url=slackWebhook)
lines = csvResults.split('\n')
if lines[0].split(",")[1][:-4]=="Révélé à" :
    resultats = "Les picks seront révélés à " + lines[0].split(",")[1][-3:] + " !"
else:
    for line in lines:
        if line != "" :
            elements = line.split(',')
            prenom = elements[0]
            if elements[1]=="" :
                resultats += prenom + " n'a pas fait son pick. Huons-le !\n"
            else :
                resultats += prenom +" a choisi *"+elements[1]+'* _[Cote : '+elements[2]+"]_\n"

slack.notify(
                text=resultats,
                icon_url="http://azerty774.free.fr/sfl_pick.png",
                username="Les picks du jour !",
                channel="sfl"
             )
