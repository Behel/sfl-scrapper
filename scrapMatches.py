from bs4 import BeautifulSoup
import requests, sys, getopt, time

##############################
# Récupération des arguments #
##############################

email = ''
password = ''
requestedDate = time.strftime("%Y-%m-%d")
# Par défaut date du jour

sys.argv.remove(sys.argv[0])
try:
    opts, args = getopt.getopt(sys.argv, 'he:p:d:')
except getopt.GetoptError:
    print('scrapMatches.py -e <email> -p <password> -d <date>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('scrapMatches.py -e <email> -p <password> -d <date>')
        sys.exit()
    elif opt == '-e':
        email = arg
    elif opt == '-p':
        password = arg
    elif opt == '-d':
        requestedDate = arg

####################
# Authentification #
####################

session = requests.Session()
payload = {'email': email, 'password': password}
URLconnection = 'http://fantasy.sofoot.com/login.php'
r = session.post(URLconnection, data=payload)


#########################################
# Récupération des compétitions du jour #
#########################################

URLcompetitions = 'http://fantasy.sofoot.com/ajax_panel2.php?date=' + requestedDate
ajaxMatches = session.get(URLcompetitions)
soup = BeautifulSoup(ajaxMatches.content, "lxml")
competitions = soup.find_all(class_="nom-competition-pick")

for competition in competitions :
    URLmatches = "http://fantasy.sofoot.com/ajax_panel3.php?competition=" + competition.string
    ajaxMatches = session.get(URLmatches)
    soupMatches = BeautifulSoup(ajaxMatches.content, "lxml")
    print(soupMatches.prettify())
    teams = soupMatches.find_all(class_="nom-pick-seul")
    cotes = soupMatches.find_all(class_="valeur-cote")
    print(teams)
    print(cotes)


