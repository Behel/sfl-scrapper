from bs4 import BeautifulSoup
import requests, sys, getopt
from util.html_table_parser import HTMLTableParser


##############################
# Récupération des arguments #
##############################

email = ''
password = ''

sys.argv.remove(sys.argv[0])
try:
    opts, args = getopt.getopt(sys.argv, 'he:p:')
except getopt.GetoptError:
    print('scrapTeamResults.py -e <email> -p <password>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('scrapTeamResults.py -e <email> -p <password>')
        sys.exit()
    elif opt == '-e':
        email = arg
    elif opt == '-p':
        password = arg


def main(_email, _password):

    retour = ""

    ####################
    # Authentification #
    ####################
    session = requests.Session()
    payload = {'email': _email, 'password': _password}
    URLconnection = 'http://fantasy.sofoot.com/login.php'
    r = session.post(URLconnection, data=payload)


    #########################################
    # Récupération des compétitions du jour #
    #########################################

    URLteam = 'http://fantasy.sofoot.com/?tpl=team'
    ajaxTeam = session.get(URLteam)
    soup = BeautifulSoup(ajaxTeam.content, "lxml")
    teamLines = str(soup.find("table"))
    p = HTMLTableParser()
    p.feed(teamLines)

    i=2
    while i < len(p.tables[0]):
        result = p.tables[0][i][4].split("(")
        retour += p.tables[0][i][1]+","+result[0][:-1]+","+result[1][:-5]+"\n"
        i+=1

    print(retour)
    return retour

if __name__ == '__main__':
    main(email, password)

