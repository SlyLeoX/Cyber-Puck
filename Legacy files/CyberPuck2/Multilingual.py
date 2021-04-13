currL = 'en'    #default language is English

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
           'Quit': 'Quit'},
    'de': {'Story': 'Geschichte',
           'Versus': 'Konfrontation',
           'Collection': 'Kollektion',
           'Settings': 'Einstellungen',
           'Credit': 'Verdienst',
           'Quit': 'Weggehen'},
    'es': {'Story': 'Historia',
           'Versus': 'Versus',
           'Collection': 'Colección',
           'Settings': 'Parámetros',
           'Credit': 'Mérito',
           'Quit': 'Dejar'}
}


def setL(selectedLanguage):
    """
    Define the language to display
    :param selectedLanguage: the language that is selected by the user
    :type str
    no return: set the language used in parameter of the set functions
    """
    global currL
    if selectedLanguage in multiL:  #verify that the selected language is one of the four proposed, technically if it is one of the keys of the dictionnary
        currL = selectedLanguage


def sysL(argv):
    """

    :param argv:
    :type
    no return:
    """
    if len(argv) >= 2:
        setL(argv[1].lower())

def transL(word):
    """

    :param word: word that we have to translate on the menu
    :type str
    :return:
    :rtype str
    """
    return multiL[currL].get(word, '***')   #to prevent if a word is not defined