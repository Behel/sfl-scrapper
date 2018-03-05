from bs4 import BeautifulSoup
import requests, sys, getopt


##############################
# Récupération des arguments #
##############################

email = ''
password = ''
# Insérez ci-dessous le nom de votre équipe
team_name="Brazilala"


sys.argv.remove(sys.argv[0])
try:
    opts, args = getopt.getopt(sys.argv, 'he:p:d:')
except getopt.GetoptError:
    print('scrapLigueEuropa.py -e <email> -p <password>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('scrapLigueEuropa.py -e <email> -p <password>')
        sys.exit()
    elif opt == '-e':
        email = arg
    elif opt == '-p':
        password = arg


def main(_email, _password,_team_name):

    retour = ""

    ####################
    # Authentification #
    ####################
    session = requests.Session()
    payload = {'email': _email, 'password': _password, 'remember': 'on'}
    URLconnection = 'http://fantasy.sofoot.com/login.php'
    session.post(URLconnection, data=payload)


    #########################################
    # Récupération des compétitions du jour #
    #########################################

    URLEuropa = 'http://fantasy.sofoot.com/?tpl=group-europa'
    ajaxMatches = session.get(URLEuropa)
    soup = BeautifulSoup(ajaxMatches.content, "lxml")

    matches_coupe = soup.find_all(class_="tournament-bracket__match")
    print(matches_coupe)
    for match in matches_coupe:
        equipes_match = match.find_all("abbr")
        if team_name == equipes_match[0].contents[0].strip() or team_name == equipes_match[1].contents[0].strip():
            score_match = match.find_all(class_="tournament-bracket__number")
            retour = equipes_match[0].contents[0].strip() + "," + score_match[0].string + '\n' \
                     + equipes_match[1].contents[0].strip() + "," + score_match[1].string

    print(retour)
    return retour

if __name__ == '__main__':
    main(email, password, team_name)

