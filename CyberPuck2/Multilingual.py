currL = 'en'

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
    currL = selectedLanguage


def sysL(argv):
    if len(argv) >= 2:
        setL(argv[1].lower())

def transL(word):
    return multiL[currL][word]