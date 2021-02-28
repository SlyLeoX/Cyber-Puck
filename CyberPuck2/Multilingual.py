from config import currL

multiL = {
    'fr': {'Story': 'Histoire',
           'Versus': '1 contre 1',
           'Collection': 'Collection',
           'Settings': 'Paramètres',
           'Credit': 'Crédit',
           'Quit': 'Quitter'},
    'en': {'Story': 'Story',
           'Versus': 'Versus',
           'Collection': 'Collection',
           'Settings': 'Settings',
           'Credit': 'Credit',
           'Quit': 'Quit'}
}


def setL(selectedLanguage):
    global currL
    print("Emma 2 ", selectedLanguage)
    currL = selectedLanguage
    print(currL)


def sysL(argv):
    if len(argv) >= 2:
        setL(argv[1].lower())
