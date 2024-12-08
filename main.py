from classes import *
import pygame
import time


# Screen variables
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
screen = 0
title = 0

# Texture variables
background = 0
sqr_button_tex = 0
rect_button_tex = 0
group = 0

# Text variables
srn_text = 0
font = 0

# Calculator variables
equation = ''
answer = ''

# Mouse variables
mouse_pos = 0

# Sets up the game window
SCREEN_WIDTH = 170
SCREEN_HEIGHT = 280

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
title = pygame.display.set_caption("Calculator")

background = pygame.image.load("img/calc.png").convert()
sqr_button_tex = pygame.image.load("img/trans square.png")
rect_button_tex = pygame.image.load("img/trans_rect.png")

# Makes the sprite group for the buttons
button_group = pygame.sprite.Group()

# USE TO MAKE BUTTONS VISIBLE
debug = pygame.Surface((30, 30))
debug_rect = pygame.Surface((70, 30))

# Makes the text
font = pygame.font.Font('digital-7.mono.ttf', 32)
srn_text = font.render(str(answer), True, (255, 255, 255))


# Adds buttons to group
def add_to_group(var):
    button_group.add(var)


# Decides what to do when a certain button is clicked
def on_click():
    global srn_text
    global equation
    global answer

    # Checks if the equation is too big
    if len(equation) > 8:
        equation = ''
        answer = "TOO BIG"
        srn_text = font.render(str(answer), True, (255, 255, 255))

    else:
        # Using 'try' instead of an 'if' allows for exception handling
        # without the app stopping and outputting an error in the console
        try:
            # Zero
            if zero_button.rect.collidepoint(mouse_pos):
                print("0 clicked")
                equation += "0"
                print(equation)

            # One
            elif one_button.rect.collidepoint(mouse_pos):
                print("1 clicked")
                equation += "1"
                print(equation)

            # Two
            elif two_button.rect.collidepoint(mouse_pos):
                print("2 clicked")
                equation += "2"
                print(equation)

            # Three
            elif three_button.rect.collidepoint(mouse_pos):
                print("3 clicked")
                equation += "3"
                print(equation)

            # Four
            elif four_button.rect.collidepoint(mouse_pos):
                print("4 clicked")
                equation += "4"
                print(equation)

            # Five
            elif five_button.rect.collidepoint(mouse_pos):
                print("5 clicked")
                equation += "5"
                print(equation)

            # Six
            elif six_button.rect.collidepoint(mouse_pos):
                print("6 clicked")
                equation += "6"
                print(equation)

            # Seven
            elif seven_button.rect.collidepoint(mouse_pos):
                print("7 clicked")
                equation += "7"
                print(equation)

            # Eight
            elif eight_button.rect.collidepoint(mouse_pos):
                print("8 clicked")
                equation += "8"
                print(equation)

            # Nine
            elif nine_button.rect.collidepoint(mouse_pos):
                print("9 clicked")
                equation += "9"
                print(equation)

            # Add
            elif plus_button.rect.collidepoint(mouse_pos):
                print("+ clicked")
                equation += "+"
                print(equation)

            # Subtract
            elif minus_button.rect.collidepoint(mouse_pos):
                print("- clicked")
                equation += "-"
                print(equation)

            # Decimal
            elif decimal_button.rect.collidepoint(mouse_pos):
                print(". clicked")
                equation += "."
                print(equation)

            # Multiply
            elif multiply_button.rect.collidepoint(mouse_pos):
                print("x clicked")
                equation += "*"
                print(equation)

            # Power button
            elif power_button.rect.collidepoint(mouse_pos):
                print("Power clicked")
                equation += "**"
                print(equation)

            # Change sign button
            elif sign_button.rect.collidepoint(mouse_pos):
                print("+ or - clicked")
                equation += "-"
                print(equation)

            # Divide
            elif divide_button.rect.collidepoint(mouse_pos):
                print("Divide clicked")
                equation += "/"
                print(equation)

            # Equals
            elif equals_button.rect.collidepoint(mouse_pos):
                print("= clicked")

                # Checks to see if an illegal operation takes place
                # If not, then the equation is calculated and outputted
                if equation[0] != '+' and equation[0] != '-' and equation[0] != '*' and equation[0] != '/':
                    answer = eval(equation)
                    answer = str(answer)[0:9]
                    print(answer)
                    srn_text = font.render(str(answer), True, (255, 255, 255))
                    screen.blit(srn_text, (15, 40))

                # If it is, then it outputs an error
                else:
                    answer = "ERROR"
                    srn_text = font.render(str(answer), True, (255, 255, 255))
                    screen.blit(srn_text, (15, 40))

            # Clear
            elif clear_button.rect.collidepoint(mouse_pos):
                print("Clear clicked")
                equation = ''
                answer = ''
                srn_text = font.render(str(answer), True, (255, 255, 255))
                screen.blit(srn_text, (15, 40))

        # If there's a syntax error, it outputs an on-screen error
        except SyntaxError:
            answer = "ERROR 1"
            srn_text = font.render(str(answer), True, (255, 255, 255))
            screen.blit(srn_text, (15, 40))

        # if the person tries to divide by 0, it outputs an on-screen error
        except ZeroDivisionError:
            answer = "ERROR 2"
            srn_text = font.render(str(answer), True, (255, 255, 255))
            screen.blit(srn_text, (15, 40))

        # If there's an index error, it outputs an on-screen error
        except IndexError:
            answer = "ERROR 3"
            srn_text = font.render(str(answer), True, (255, 255, 255))
            screen.blit(srn_text, (15, 40))

        # If the user tries to do math that is beyond what python can do,
        # It outputs an on-screen error if it doesn't crash.
        except OverflowError:
            answer = "ERROR 4"
            srn_text = font.render(str(answer), True, (255, 255, 255))
            screen.blit(srn_text, (15, 40))


# Makes the sprite for the buttons and adds them to a group
# Zero
zero_button = Button(sqr_button_tex, 10, 240, on_click)
add_to_group(zero_button)
# One
one_button = Button(sqr_button_tex, 10, 200, on_click)
add_to_group(one_button)
# Two
two_button = Button(sqr_button_tex, 50, 200, on_click)
add_to_group(two_button)
# Three
three_button = Button(sqr_button_tex, 90, 200, on_click)
add_to_group(three_button)
# Four
four_button = Button(sqr_button_tex, 10, 160, on_click)
add_to_group(four_button)
# Five
five_button = Button(sqr_button_tex, 50, 160, on_click)
add_to_group(five_button)
# Six
six_button = Button(sqr_button_tex, 90, 160, on_click)
add_to_group(six_button)
# Seven
seven_button = Button(sqr_button_tex, 10, 120, on_click)
add_to_group(seven_button)
# Eight
eight_button = Button(sqr_button_tex, 50, 120, on_click)
add_to_group(eight_button)
# Nine
nine_button = Button(sqr_button_tex, 90, 120, on_click)
add_to_group(nine_button)
# Add
plus_button = Button(sqr_button_tex, 130, 160, on_click)
add_to_group(plus_button)
# Subtract
minus_button = Button(sqr_button_tex, 130, 200, on_click)
add_to_group(minus_button)
# Decimal
decimal_button = Button(sqr_button_tex, 50, 240, on_click)
add_to_group(decimal_button)
# Multiply
multiply_button = Button(sqr_button_tex, 130, 120, on_click)
add_to_group(multiply_button)
# Power
power_button = Button(sqr_button_tex, 50, 80, on_click)
add_to_group(power_button)
# Change sign
sign_button = Button(sqr_button_tex, 90, 80, on_click)
add_to_group(sign_button)
# Divide
divide_button = Button(sqr_button_tex, 130, 80, on_click)
add_to_group(divide_button)
# Equals
equals_button = Button(rect_button_tex, 90, 240, on_click)
add_to_group(equals_button)
# Clear
clear_button = Button(sqr_button_tex, 10, 80, on_click)
add_to_group(clear_button)

# Main loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Displays background image
    button_group.update(events)
    screen.blit(background, (0, 0))

    # Displays the current equation
    screen.blit(font.render(str(equation), True, (255, 255, 255)), (15, 15))
    screen.blit(srn_text, (15, 40))

    button_group.draw(screen)
    pygame.display.update()
