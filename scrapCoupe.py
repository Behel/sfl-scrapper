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
    print('scrapCoupe.py -e <email> -p <password>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('scrapCoupe.py -e <email> -p <password>')
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
    payload = {'email': _email, 'password': _password, 'remember': 'on'}
    URLconnection = 'http://fantasy.sofoot.com/login.php'
    session.post(URLconnection, data=payload)


    #########################################
    # Récupération des compétitions du jour #
    #########################################

    URLcompetitions = 'http://fantasy.sofoot.com/ajax_panel1.php'
    ajaxMatches = session.get(URLcompetitions)
    soup = BeautifulSoup(ajaxMatches.content, "lxml")

    equipes_coupe = soup.find(class_="list-group-bordered").find_all(class_="list-group-item")
    for equipe in equipes_coupe:
        place = equipe.find('strong')
        score = equipe.find(class_="badge")
        name = equipe.find('a')
        retour += place.string[:-1]+','+name.string+','+score.string[:-4]+'\n'


    print(retour)
    return retour

if __name__ == '__main__':
    main(email, password)

