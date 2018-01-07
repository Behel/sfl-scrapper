import slackweb, time, os
import scrapTeamResults

##############################
# Récupération des arguments #
##############################

email = os.getenv('sfl_email')
password = os.getenv('sfl_password')
requestedDate = time.strftime("%Y-%m-%d")
slackWebhook = os.getenv('sfl_slackwebhook')

csvResults = scrapTeamResults.main(email, password)
resultats = ''
slack = slackweb.Slack(url=slackWebhook)
lines = csvResults.split('\n')
for line in lines:
    if line != "" :
        elements = line.split(',')
        prenom = elements[0]
        if elements[1]=="" :
            resultats += prenom + " n'a pas fait son pick. Huons-le !\n"
        elif elements[2]=="0" :
            resultats += prenom + " *n'a pas gagné de points* en choisissant _" + elements[1] + "_. Bad Pick\n"
        elif int(elements[2])>50 :
            resultats += "*GOLDEN PIF* pour "+ prenom + " en choisissant _" + elements[1] + "_. Ca fait *"+elements[2]+"* points dans la cagnotte.\n"
        else :
            resultats += prenom+" : + *"+ elements[2] +"* en choisissant _"+elements[1]+"_\n"

slack.notify(
                text=resultats,
                icon_url="http://azerty774.free.fr/sfl_results.png",
                username="Les résultats d'hier !",
                channel="sfl"
             )
