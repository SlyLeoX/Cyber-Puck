import pygame

"""
Code to add to get_input
if __name__ == '__main__':
    while 1:
        pygame.init()

        clock = pygame.time.Clock()
        clock.tick(20)

        pygame.joystick.init()
        joystick = []
        for i in range(pygame.joystick.get_count()):
            joystick.append(pygame.joystick.Joystick(i))
            joystick[-1].init()

        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION and event.instance_id == self.number - 1:
                if event.axis in self.map_axis:
                    if event.value == 1:
                        self.inputs[self.map_axis[axis]] = "pressed"
                    else:
                        self.inputs[self.map_axis[axis]] = "released"
                else:
                    self.inputs_axis[event.axis] = event.value
            if event.type == pygame.JOYABUTTONDOWN and event.instance_id == self.number - 1:
                if event.value in self.map.values():
                    self.inputs[event.value] = "pressing"
            if event.type == pygame.JOYABUTTONUP and event.instance_id == self.number - 1:
                if event.value in self.map.values():
                    self.inputs[event.value] = "releasing"
        for input in self.inputs:
            if self.inputs[input] == "pressing":
                self.inputs[input] == "pressed"
            if self.inputs[input] == "releasing":
                del(self.inputs[input])
"""

# self.map = {action : key}
# self.map_axis = {axis number : corresponding action}
# self.inputs = {action : "pressed"/"pressing"/"released"}
# self.inputs_axis = {axis number : value}


"""
Du coup il faut faire une boucle après avoir utilisé les inputs pour 2 choses :
        for input in self.inputs:
            if self.inputs[input] == "pressing":
                self.inputs[input] == "pressed"
            if self.inputs[input] == "releasing":
                del(self.inputs[input])
"""

# To improve :
# We should get how long we will take to reset to our original position given our speed, and maybe try to acccount
# for speed on arrival ? idk if it should be done here or when we use that function

def get_quickest_position(player_x_pos, player_y_pos, max_speed, ball_x_pos, ball_y_pos, ball_x_speed, ball_y_speed):
    # Takes in the necessary parameters, returns the position that we must go to
    # In the future, I may change it to just take the player and the ball as arguments if I can do that with attributes

    # Max speed in pix per frame
    catchable = False
    radius = 0
    # First we get the ball position that we can reach
    while not catchable:
        radius += max_speed
        ball_x_pos += ball_x_speed
        if ball_x_pos > 768:
            ball_x_pos += 786 - ball_x_pos
        if ball_x_pos > 1366:
            ball_x_pos += 1366 - ball_x_pos
        if radius > ((ball_x_pos - player_x_pos) ** 2 + (ball_y_pos - player_y_pos) ** 2) ** (1 / 2):
            catchable = True

    # Then we go where the ball will be 10 frames after that

    player_x_pos, player_y_pos = ball_x_pos, ball_y_pos
    for i in range(10):
        player_x_pos += ball_x_speed
        player_y_pos = ball_y_speed
        if player_x_pos > 768:
            player_x_pos += 786 - player_x_pos
        if player_y_pos > 1366:
            player_y_pos += 1366 - player_y_pos

    # We return that position
    return (player_x_pos, player_y_pos)


if __name__ == '__main__':
    print("hello world")