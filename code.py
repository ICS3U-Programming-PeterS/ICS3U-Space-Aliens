#!/usr/bin/env python3


# Created by: Peter Sobowale
# Created on: Jan 2023
# This program is the "Space Aliens" game for the PyBadge.
import ugame
import stage
import random
import time
import supervisor
import constants
import os


# global variable off
mute = "off"


def splash_scene(mute):
    # This function sets up and runs the splash scene.

    # get coin sound ready
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # play coin sound
    sound.play(coin_sound)

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # tile the background to make a splash screen
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and ball to the layers list
    game.layers = [background]

    # Draw the background on the screen
    game.render_block()

    # repeat forever game loop
    while True:
        # wait for 2 seconds
        time.sleep(2)

        # go to the menu scene
        menu_scene()


def instructions_scene():
    # This function displays the instructions scene
    # It also allows the user to go back to the menu scene
    # Load the image "pingpong_background.bmp"
    image_bank_2 = stage.Bank.from_bmp16("pingpong_background.bmp")

    # Create a background object using the image and dimensions from constants
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # set the background tile to choose random background from 1 - 3
    # using nested for each loops
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 1)

    # Display the instructions
    print("INSTRUCTIONS")
    print("\nWin if you get high \nscore, lose if you don't\n")
    print("Press A to return \nto menu.")

    # Create a "Stage" object to manage the game graphics and input
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and text objects to the layers list
    game.layers = [background]

    # Draw the background and text on the screen
    game.render_block()

    while True:
        # Check for user input
        keys = ugame.buttons.get_pressed()

        # check if they pressed the start button
        if keys & ugame.K_START != 0:
            # go to game scene
            game_scene(mute)

        # check if they pressed the A button
        if keys & ugame.K_O != 0:
            # go to menu scene
            menu_scene()

        # Pause the loop to achieve 60fps frame rate
        game.tick()


def menu_scene():
    # This function sets up and runs the menu scene.

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens.bmp")

    # Add text objects (into a list)
    text = []

    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text1 = stage.Text(
        width=29,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )

    # Move the text to the position (17, 20)
    text1.move(17, 20)

    # Set the text to "Ping Pong Escape"
    text1.text("Ping Pong Escape")

    # Add the text object to the text list
    text.append(text1)

    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # Move the text to the position (32, 110)
    text2.move(32, 110)

    # Set the text to "START TO PLAY"
    text2.text("START TO PLAY")

    # Add the text object to the text list
    text.append(text2)

    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # Move the text to the position (8, 70)
    text3.move(8, 70)

    # Set the text to "PRESS START"
    text3.text("B FOR INSTRUCTIONS")

    # Add the text object to the text list
    text.append(text3)

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and ball to the layers list
    game.layers = text + [background]

    # Draw the background on the screen
    game.render_block()

    # Game Loop
    while True:
        # for user input
        keys = ugame.buttons.get_pressed()

        # Check if they press the start button
        if keys & ugame.K_START != 0:
            # go to the game scene
            game_scene(mute)

        # check if they press the B button
        if keys & ugame.K_X != 0:
            # go to the instructions scene
            instructions_scene()

        # Pause the loop to achieve 60fps frame rate
        game.tick()


# This function sets up and runs the main game scene.
def game_scene(mute):
    # Set the score to 0
    score = 0

    # Display the score in the top left corner
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    # display if mute on/off in the top left corner
    mute_text = stage.Text(width=29, height=14)
    mute_text.clear()
    mute_text.cursor(0, 0)
    mute_text.move(1, 9)
    mute_text.text("Mute: {0}".format(mute))

    # this function takes an alien off screen and makes it move on screen
    def show_alien():
        # for loop to cycle through all the aliens
        for alien_number in range(len(aliens)):
            # check if they are not on the screen
            if aliens[alien_number].x < 0:
                # move them on the screen
                aliens[alien_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("pingpong_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Buttons state information.
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound file ready.
    pew_sound = open("pew.wav", "rb")
    pingpong_sound = open("pingpong.wav", "rb")
    boom_sound = open("boom.wav", "rb")
    crash_sound = open("crash.wav", "rb")
    sound = ugame.audio
    sound.stop()

    # Unmute it
    sound.mute(False)

    # create list of lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        lasers.append(a_single_laser)

    # create 5 aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        # spawn them off the screen
        a_single_alien = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        aliens.append(a_single_alien)

    # place 1 alien on the screen
    show_alien()

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # set the background tile to choose random background from 1 - 3
    # do this using nested for each loops
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    # Create the ball sprite using image at index 5
    ball = stage.Sprite(
        image_bank_sprites,
        5,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        56,
    )

    # create a table sprite
    table = stage.Sprite(image_bank_sprites, 0, 0, 56)

    # create a second table sprite
    table2 = stage.Sprite(
        image_bank_sprites, 0, constants.SCREEN_X - constants.SPRITE_SIZE, 56
    )

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background, lasers and other sprites to the layers list
    game.layers = (
        [score_text]
        + [mute_text]
        + lasers
        + [ball]
        + [table, table2]
        + aliens
        + [background]
    )

    # Draw the background on the screen
    game.render_block()

    # Game Loop
    while True:
        # for user input
        keys = ugame.buttons.get_pressed()

        # A button for fire.
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # B button to fire
        if keys & ugame.K_X != 0:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        # if they press select
        if keys & ugame.K_SELECT != 0:
            if select_button == constants.button_state["button_up"]:
                select_button = constants.button_state["button_just_pressed"]
            elif select_button == constants.button_state["button_just_pressed"]:
                select_button = constants.button_state["button_still_pressed"]
        else:
            if select_button == constants.button_state["button_still_pressed"]:
                select_button = constants.button_state["button_released"]
            else:
                select_button = constants.button_state["button_up"]

        # if they press the start button
        if keys & ugame.K_START != 0:
            pass

        # code to move ball sprite to the right
        if keys & ugame.K_RIGHT != 0:
            if ball.x < constants.SCREEN_X - constants.SPRITE_SIZE:
                ball.move(ball.x + 1, ball.y)
            else:
                ball.move(constants.SCREEN_X - constants.SPRITE_SIZE, ball.y)

        # code to move ball sprite to the left
        if keys & ugame.K_LEFT != 0:
            if ball.x >= 0:
                ball.move(ball.x - 1, ball.y)
            else:
                ball.move(0, ball.y)

        # code to move ball sprite up and to wrap it
        if keys & ugame.K_UP != 0:
            if ball.y >= 0:
                ball.move(ball.x, ball.y - 1)
            else:
                ball.move(ball.x, 120)

        # code to move ball sprite to the down and to wrap it
        if keys & ugame.K_DOWN != 0:
            if ball.y <= 120:
                ball.move(ball.x, ball.y + 1)
            else:
                ball.move(ball.x, 0)

        # update game logic
        # play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # fire a laser, if we have enough power (have not used up all the lasers)
            for laser_number in range(len(lasers)):
                # check if the laser are on the screen
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ball.x, ball.y)
                    # if mute is off then play the sound
                    if mute == "off":
                        sound.play(pew_sound)
                        break
                    else:
                        break

        # if the b button is pressed play sound if mute is off
        if b_button == constants.button_state["button_just_pressed"]:
            if mute == "off":
                sound.play(pingpong_sound)
            else:
                pass

        # if the select button is pressed
        if select_button == constants.button_state["button_just_pressed"]:

            # if it isn't muted, mute it
            if mute == "off":
                mute = "on"
                mute_text.clear()
                mute_text.cursor(0, 0)
                mute_text.move(1, 9)
                mute_text.text("Mute: {0}".format(mute))

            # if it is muted , unmute it
            else:
                mute = "off"
                mute_text.clear()
                mute_text.cursor(0, 0)
                mute_text.move(1, 9)
                mute_text.text("Mute: {0}".format(mute))

        # each frame move the lasers, that have been fired up
        for laser_number in range(len(lasers)):

            # only if the laser is on the screen
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )

                # if the laser y coordinate is less than -16
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # each frame move the alien down that are on the screen
        for alien_number in range(len(aliens)):
            # check to make sure it is on the screen
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(
                    aliens[alien_number].x,
                    aliens[alien_number].y + constants.ALIEN_SPEED,
                )

                # if the alien goes off the screen go to spawn point (-100,-100)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

                    # display 1 alien
                    show_alien()

                    # decrease score by 1 if the alien gets to the bottom
                    score -= 1
                    if score < 0:
                        score = 0

                    # display the score
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(
                            lasers[laser_number].x + 4,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11,
                            lasers[laser_number].y + 12,
                            aliens[alien_number].x,
                            aliens[alien_number].y + 6,
                            aliens[alien_number].x + 15,
                            aliens[alien_number].y + 15,
                        ):
                            # You hit an alien
                            # Move the alien & laser off screen
                            aliens[alien_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            lasers[laser_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )

                            # Stop any currently playing sound
                            sound.stop()
                            # Play the sound of the alien being hit
                            if mute == "off":
                                sound.play(boom_sound)
                            else:
                                pass
                            # Show two new aliens on the screen
                            show_alien()
                            show_alien()
                            # Increase the score by 1
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))

            for alien_number in range(len(aliens)):
                # Check if the x-coordinate of the alien is greater than 0, meaning it is on the screen
                if aliens[alien_number].x > 0:
                    # Check for collision between the current alien and the ship using the `stage.collide` function
                    # This function takes the x and y coordinates of the bounding box of each object
                    # In this case, the bounding box of the alien is defined as x+1, y, x+15, y+15
                    # and the bounding box of the ship is defined as ship.x, ship.y, ship.x + 15, ship.y + 15
                    if stage.collide(
                        aliens[alien_number].x + 2,
                        aliens[alien_number].y + 2,
                        aliens[alien_number].x + 15,
                        aliens[alien_number].y + 15,
                        ball.x + 7,
                        ball.y + 7,
                        ball.x + 8,
                        ball.y + 15,
                    ):
                        # If collision is detected, stop any currently playing sound
                        sound.stop()
                        # Play the crash sound
                        if mute == "off":
                            sound.play(crash_sound)
                        else:
                            pass
                        # Wait for 3 seconds before moving on to the game over scene
                        time.sleep(3.0)
                        # Call the game over scene and pass in the current score

                        # my personal high score
                        high_score = 64

                        # Check if the current score is higher than the high score
                        if score > high_score:
                            game_win_scene(score, high_score)
                        else:
                            game_loss_scene(score, high_score)

        # Redraw the Sprites
        game.render_sprites(lasers + [ball] + [table, table2] + aliens)

        # Pause the loop to achieve 60fps frame rate
        game.tick()


def game_loss_scene(final_score, high_score):
    # This function displays the game over scene with the final score and
    # allows the user to restart the game by pressing the SELECT button.
    # Load the image "mt_game_studio.bmp"
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create a background object using the image and dimensions from constants
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Create a list to store text objects
    text = []

    text5 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (20, 20)
    text5.move(20, 35)
    # Set the text to the final score
    text5.text("High Score: {:0>2d}".format(high_score))
    # Add the text object to the text list
    text.append(text5)

    # Create a Text object with a width of 29, height of 14, no font, and the blue palette
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (20, 20)
    text1.move(20, 20)
    # Set the text to the final score
    text1.text("Final Score: {:0>2d}".format(final_score))
    # Add the text object to the text list
    text.append(text1)

    # Create a Text object with a width of 29, height of 14, no font, and the blue palette
    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (43, 60)
    text2.move(43, 60)
    # Set the text to "GAME OVER"
    text2.text("GAME OVER")
    # Add the text object to the text list
    text.append(text2)

    text4 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (43, 60)
    text4.move(48, 70)
    # Set the text to "GAME OVER"
    text4.text("YOU LOSE")
    # Add the text object to the text list
    text.append(text4)

    # Create a Text object with a width of 29, height of 14, no font, and the blue palette
    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (32, 110)
    text3.move(32, 110)
    # Set the text to "PRESS SELECT"
    text3.text("PRESS SELECT")
    # Add the text object to the text list
    text.append(text3)

    # Create a "Stage" object to manage the game graphics and input
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and text objects to the layers list
    game.layers = text + [background]

    # Draw the background and text on the screen
    game.render_block()

    while True:
        # Check if the SELECT button is pressed
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            has_reloaded = True
            # Reload the game if SELECT is pressed
            supervisor.reload()

        game.tick()


def game_win_scene(current_score, high_score):
    # This function displays the game over scene with the final score and

    # allows the user to restart the game by pressing the SELECT button.

    # Load the image "mt_game_studio.bmp"
    image_bank_2 = stage.Bank.from_bmp16("pingpong_background.bmp")

    # Create a background object using the image and dimensions from constants
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Create a list to store text objects
    text = []

    # Create a Text object with a width of 29, height of 14, no font, and the blue palette
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (20, 20)
    text1.move(20, 20)
    # Set the text to the final score
    text1.text("Final Score: {:0>2d}".format(current_score))
    # Add the text object to the text list
    text.append(text1)

    # Create a Text object with a width of 29, height of 14, no font, and the blue palette
    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (43, 60)
    text2.move(43, 60)
    # Set the text to "GAME OVER"
    text2.text("GAME OVER")
    # Add the text object to the text list
    text.append(text2)

    text4 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (43, 60)
    text4.move(48, 70)
    # Set the text to "GAME OVER"
    text4.text("YOU WIN")
    # Add the text object to the text list
    text.append(text4)

    # Create a Text object with a width of 29, height of 14, no font, and the blue palette
    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (32, 110)
    text3.move(32, 110)
    # Set the text to "PRESS SELECT"
    text3.text("PRESS SELECT")
    # Add the text object to the text list
    text.append(text3)

    # Create a "Stage" object to manage the game graphics and input
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and text objects to the layers list
    game.layers = text + [background]

    # Draw the background and text on the screen
    game.render_block()

    while True:
        # Check if the SELECT button is pressed
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            has_reloaded = True
            # Reload the game if SELECT is pressed
            supervisor.reload()

        game.tick()


if __name__ == "__main__":
    splash_scene(mute)
