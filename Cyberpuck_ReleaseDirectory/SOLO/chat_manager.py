import pygame


# That function loads the right character arts according to the file's first line.
def replica_init(dialogue):
    characters = dialogue[0].removesuffix("\n").split(",")
    # print(characters)
    portraits = {}
    for loading in characters:
        path = r"CORE\ressources\characters\fix".removesuffix("fix") + loading + "\icon.png"
        # print(path)
        portraits[loading] = (pygame.image.load(path).convert_alpha())
    portraits[characters[1]] = pygame.transform.flip(portraits[characters[1]], True, False)
    return portraits

# Just blitting the arts at each loop.
def blit_portraits(system_parameters, portraits):
    portrait_L = portraits[0]
    portrait_R = portraits[1]

    screen = system_parameters[0]
    width = system_parameters[1][0]
    height = system_parameters[1][1]

    screen.blit(portrait_L, (width * 1 / 12, height * 2 / 12))
    screen.blit(portrait_R, ((width * 11 / 12) - (portrait_R.get_rect().size)[0], height * 2 / 12))


# Blitting the replicas as well as the speech bubble.
def replica_blitting(system_parameters, dialogue, portraits, line):
    black = (0, 0, 0)

    screen = system_parameters[0]
    width = system_parameters[1][0]
    height = system_parameters[1][1]

    replica = dialogue[line].split(":")
    # print(replica)

    # Don't forget to put that line at the end of the dialog file so the code spots the end of the dialog.
    if replica[0] == "#END":
        return -1

    # The 'orientation' of the speech bubble is linked to what character is talking according to the dialog file.
    if replica[0] == list(portraits.keys())[0]:
        orientation = "left"
    else:
        orientation = "right"

    bubble = pygame.image.load(r"CORE\ressources\ui\speaker_bubble_slim.png").convert_alpha()
    bubble = pygame.transform.scale(bubble, (int(3840 / 6), int(960 / 6)))
    if orientation == "right": bubble = pygame.transform.flip(bubble, True, False)

    bubble_rect = bubble.get_rect()
    (bubble_rect.centerx, bubble_rect.centery) = ((width * 1 / 2), (height * 1 / 2))

    screen.blit(bubble, bubble_rect)

    # The texts should be written in a way so the replicas doesn't go overboard of the speech bubble, put - to break.
    replica = replica[1].split("-")
    for i in range(len(replica)):
        misc_text = pygame.font.SysFont('Calibri', int(960/56))
        misc_text = misc_text.render(replica[i].removesuffix("\n"), False, black)
        screen.blit(misc_text, bubble_rect.move(32, 64+(int(960/32)*i)))

    return line

# This code allow to detect if the player presses any key.
def press(last_press):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            return True
    return False


# Allows to display a dialogue between 2 characters with the dialogue located in a file and a set background.
def chat(system_parameters, code, bg):

    screen = system_parameters[0]

    # The "code" is directly the name of the file containing the dialog (without the .txt)
    dialogue_file_path = (r"SOLO\dialogues\dial_fr\fix".removesuffix("fix"))+str(code)+".txt"
    dialogue_file = open(dialogue_file_path, "r", encoding="UTF-8")
    dialogue = dialogue_file.readlines()

    bg = pygame.image.load(bg).convert_alpha()
    bg = pygame.transform.scale(bg, system_parameters[1])

    portraits = replica_init(dialogue)
    line = 1
    last_press = 0
    # The dialog is an independent loop in itself. Could be optimized and turned into a plain diaporama.
    while 1:
        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))
        blit_portraits(system_parameters, list(portraits.values()))
        line = replica_blitting(system_parameters, dialogue, portraits, line)
        # print(line)
        if line == -1:
            break
        if press(last_press):
            line += 1

        pygame.display.flip()

    # print("Dialogue has ended!")