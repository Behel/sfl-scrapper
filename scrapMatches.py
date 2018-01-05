from bs4 import BeautifulSoup
import requests, sys, getopt, time

##############################
# Récupération des arguments #
##############################

email = ''
password = ''
requestedDate = time.strftime("%Y-%m-%d")
# Par défaut date du jour

try:
    opts, args = getopt.getopt(sys.argv, "hepd:")
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
session.post(URLconnection, data=payload)


#########################################
# Récupération des compétitions du jour #
#########################################

URLcompetitions = 'http://fantasy.sofoot.com/ajax_panel2.php?date=' + requestedDate
ajaxCompetitions = session.get(URLcompetitions)
soup = BeautifulSoup(ajaxCompetitions.content, "lxml")
print(soup.prettify())

