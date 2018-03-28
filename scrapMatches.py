from bs4 import BeautifulSoup
import requests, sys, getopt, time


##############################
# Recuperation des arguments #
##############################

email = ''
password = ''
requestedDate = time.strftime("%Y-%m-%d")
# Par defaut date du jour

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


def main(_email, _password, _requesteddate):

    retour = ""

    ####################
    # Authentification #
    ####################
    session = requests.Session()
    payload = {'email': _email, 'password': _password, 'remember': 'on'}
    URLconnection = 'http://fantasy.sofoot.com/login.php'
    session.post(URLconnection, data=payload)


    #########################################
    # Recuperation des competitions du jour #
    #########################################

    URLcompetitions = 'http://fantasy.sofoot.com/ajax_panel2.php?date=' + _requesteddate
    ajaxMatches = session.get(URLcompetitions)
    soup = BeautifulSoup(ajaxMatches.content, "lxml")
    competitions = soup.find_all(class_="nom-competition-pick")

    for competition in competitions :
        URLmatches = "http://fantasy.sofoot.com/ajax_panel3.php?competition=" + competition.string
        ajaxMatches = session.get(URLmatches)
        soupMatches = BeautifulSoup(ajaxMatches.content, "lxml")
        teams = soupMatches.find_all(class_="nom-pick-seul")
        cotes = soupMatches.find_all("b")
        i = 0
        while i < len(teams):
            retour+=(competition.string + ','
                          + teams[i].string + ',' + cotes[i].string + ','
                          + teams[i + 1].string + ',' + cotes[i + 1].string + '\n')
            i += 2

    print(retour)
    return retour

if __name__ == '__main__':
    main(email, password, requestedDate)

