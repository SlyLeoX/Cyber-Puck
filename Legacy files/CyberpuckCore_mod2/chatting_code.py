import pygame

# READ MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# This code is currently unused, don't touch it!

if __name__ == '__main__':

    pygame.init()
    size = width, height = 1366, 768
    screen = pygame.display.set_mode(size)

    # The file give the characters to show with its header ?

    dialogue_file = 'dialogues\dial_fr\dial_test.txt'
    dialogue_file = open(dialogue_file, "r", encoding="UTF-8")
    dialogue = dialogue_file.readlines()

    def replica_init(dialogue):
        characters = dialogue[0].removesuffix("\n").split(",")
        print(characters)
        portraits = {}
        for loading in characters:
            portraits[loading] = (pygame.image.load(r"ressources\characters\sanic\icon.gif").convert_alpha())
        portraits[characters[1]] = pygame.transform.flip(portraits[characters[1]],True,False)
        return portraits

    def blit_portraits(portraits):
        portrait_L = portraits[0]
        portrait_R = portraits[1]

        screen.blit(portrait_L, (width*1/12,height*1/6))
        screen.blit(portrait_R, ((width*11/12)-(portrait_R.get_rect().size)[0],height*1/6))

    def replica_blitting(portraits, line):
        replica = dialogue[line].split(":")
        print(replica)

        if replica[0] == list(portraits.keys())[0]: orientation = "left"
        else: orientation = "right"

        bubble = pygame.image.load(r"ressources\ui\speaker_bubble_slim.png").convert_alpha()
        bubble = pygame.transform.scale(bubble, (int(3840/6),int(960/6)))
        if orientation == "right": bubble = pygame.transform.flip(bubble, True, False)

        bubble_rect = bubble.get_rect()
        (bubble_rect.centerx, bubble_rect.centery) = ((width * 1/2), (height * 1 / 2))

        screen.blit(bubble, bubble_rect)

        black = (0, 0, 0)
        misc_text = pygame.font.SysFont('Calibri', int(960/32))
        misc_text = misc_text.render(replica[1].removesuffix("\n"), False, black)
        screen.blit(misc_text, bubble_rect.move(32,64))

        if replica[0] == "#END\n":
            return -1
        else:
            return line


    def press(last_press):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                return True
        return False


    portraits = replica_init(dialogue)
    line = 1
    last_press = 0
    while 1:
        screen.fill((255,255,255))
        blit_portraits(list(portraits.values()))
        line = replica_blitting(portraits, line)
        print(line)
        if line == -1:
            break
        if press(last_press):
            line += 1

        pygame.display.flip()

    print("Dialogue has ended!")
