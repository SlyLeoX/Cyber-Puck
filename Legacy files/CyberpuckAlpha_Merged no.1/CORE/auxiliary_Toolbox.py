import pygame
from time import sleep

# Allow to get the colors from a string without using a if chain.
color_code = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (175, 0, 0), "green": (0, 175, 0),
                  "blue": (0, 0, 175)}


# Displays a text on the screen with a frame around during a given time.
def text_box(system_parameters, text, color, time):

    screen = system_parameters[0]
    width = system_parameters[1][0]
    height = system_parameters[1][1]

    red = 255, 0, 0

    font = '8-BIT WONDER.TTF'
    full_font = pygame.font.Font(font, 80)
    full_text = full_font.render(text, True, color_code[color])
    text_size = full_font.size(text)
    text_pos = ((width / 2) - (text_size[0] / 2), (height / 2) - (text_size[1] / 2))

    box = pygame.image.load(r"CORE\ressources\ui\speakerless_bubble.png").convert_alpha()
    box = pygame.transform.scale(box, (text_size[0] + 120, text_size[1] + 120))

    box_rect = box.get_rect()
    box_rect.x = (width / 2) - (text_size[0] / 2) - 65
    box_rect.y = (height / 2) - (text_size[1] / 2) - 60

    screen.blit(box, box_rect)
    screen.blit(full_text, text_pos)

    pygame.display.flip()

    pygame.time.wait(time)
    # sleep(time/1000)


# Displays a text on the screen with a uniform color on the whole screen behind during a given time.
def text_screen(system_parameters, text, color, time, size=80):

    screen = system_parameters[0]
    width = system_parameters[1][0]
    height = system_parameters[1][1]

    # Associate the chosen background color with an appropriate font color.
    color_link = {"white": "black", "black": "white", "red": "black", "green": "white", "blue": "white"}

    screen.fill(color_code[color])

    font = '8-BIT WONDER.TTF'
    full_font = pygame.font.Font(font, size)

    # The texts should be written in a way so the replicas doesn't go overboard of the speech bubble, put - to break.
    text = text.split("-")
    for i in range(len(text)):
        full_text = full_font.render(text[i], True, color_code[color_link[color]])
        text_size = full_font.size(text[i])
        text_pos = ((width / 2) - (text_size[0] / 2), (height / 2) - (text_size[1] / 2))
        screen.blit(full_text, (text_pos[0], text_pos[1]+100*i))

    pygame.display.flip()

    pygame.time.wait(time)
    # sleep(time/1000)


# Displays text as paragraphs on the screen for easier printing of long texts.
def story_text_screen(system_parameters, lines, color, size=40):

    screen = system_parameters[0]
    width = system_parameters[1][0]
    height = system_parameters[1][1]

    # Associate the chosen background color with an appropriate font color.
    color_link = {"white": "black", "black": "white", "red": "black", "green": "white", "blue": "white"}

    screen.fill(color_code[color])

    # font = '8-BIT WONDER.TTF'
    used_font = 'Perfect DOS VGA 437 Win.ttf'
    # used_font = None

    full_font = pygame.font.Font(used_font, size)

    reading = True
    for i in range(0, len(lines), 10):

        if (len(lines)-i)>10:
            printed = 10
        else:
            printed = len(lines) - i

        while reading :
            screen.fill(color_code[color])
            for j in range(printed):
                full_text = full_font.render(lines[i+j].removesuffix("\n"), True, color_code[color_link[color]])
                text_pos = ((width / 24), (height / 12) + (j*30))
                screen.blit(full_text, text_pos)

            full_text = full_font.render("[PRESS A KEY TO CONTINUE]", True, color_code[color_link[color]])
            text_pos = ((width / 24), (height / 12) + ((1+printed) * 30))
            screen.blit(full_text, text_pos)
            pygame.display.flip()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    reading = False
        reading = True
        print(i,len(lines))