import slackweb, time, os
import scrapMatches

##############################
# Récupération des arguments #
##############################

email = os.getenv('sfl_email')
password = os.getenv('sfl_password')
requestedDate = time.strftime("%Y-%m-%d")
slackWebhook = os.getenv('sfl_slackwebhook')

csvMatches = scrapMatches.main(email, password, requestedDate)
matchesDuJour = ''
slack = slackweb.Slack(url=slackWebhook)
competitionPrec = ''
lines = csvMatches.split('\n')
for line in lines:
    if line != "" :
        elements = line.split(',')
        print(elements)
        if elements[0] != competitionPrec :
            matchesDuJour += "\nEn *"+elements[0]+"* : \n"
            competitionPrec = elements[0]
        matchesDuJour += "  "+elements[1]+" _("+elements[2]+")_ vs "+elements[3]+" _("+elements[4]+")_\n"

slack.notify(
                text=matchesDuJour,
                icon_url="http://azerty774.free.fr/sfl_calendar.png",
                username="Les matches du jour !",
                channel="sfl"
             )
