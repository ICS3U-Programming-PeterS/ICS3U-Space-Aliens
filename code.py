#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Jan 2023
# This program is the "Space Aliens" game for the PyBadge.
import stage
import ugame

import constants


def menu_scene():
    # This function sets up and runs the menu scene.

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens.bmp")

    # Add text objects
    text = []

    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text1 = stage.Text(
        width=29,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )

    # Move the text to the position (20, 10)
    text1.move(25, 10)

    # Set the text to "MT Game Studio"
    text1.text("Sobowale Studio")

    # Add the text object to the text list
    text.append(text1)

    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (40, 110)
    text2.move(40, 110)
    # Set the text to "PRESS START"
    text2.text("PRESS START")
    # Add the text object to the text list
    text.append(text2)

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
        if keys & ugame.K_START:
            game_scene()

        # Pause the loop to achieve 60fps frame rate
        game.tick()


def game_scene():
    # This function sets up and runs the main game scene.

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
    coin_sound = open("pingpong.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Create the ball sprite using image at index 5, with initial position
    # (56,57)
    ball = stage.Sprite(
        image_bank_sprites,
        5,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        56,
    )
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )
    table = stage.Sprite(image_bank_sprites, 0, 0, 56)
    table2 = stage.Sprite(
        image_bank_sprites, 0, constants.SCREEN_X - constants.SPRITE_SIZE, 56
    )

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and ball to the layers list
    game.layers = [ball] + [table, table2, alien] + [background]

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

        if keys & ugame.K_START:
            pass

        if keys & ugame.K_SELECT:
            pass

        # code to move ball sprite and to rap it
        if keys & ugame.K_RIGHT != 0:
            if ball.x < constants.SCREEN_X - constants.SPRITE_SIZE:
                ball.move(ball.x + 1, ball.y)
            else:
                ball.move(constants.SCREEN_X - constants.SPRITE_SIZE, ball.y)

        if keys & ugame.K_LEFT != 0:
            if ball.x >= 0:
                ball.move(ball.x - 1, ball.y)
            else:
                ball.move(0, ball.y)

        if keys & ugame.K_UP != 0:
            if ball.y >= 0:
                ball.move(ball.x, ball.y - 1)
            else:
                ball.move(ball.x, 120)

        if keys & ugame.K_DOWN != 0:
            if ball.y <= 120:
                ball.move(ball.x, ball.y + 1)
            else:
                ball.move(ball.x, 0)

        # update game logic
        # play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        if b_button == constants.button_state["button_just_pressed"]:
            sound.play(coin_sound)

        # Redraw the Sprites
        game.render_sprites([ball] + [table, table2, alien])

        # Pause the loop to achieve 60fps frame rate
        game.tick()


if __name__ == "__main__":
    menu_scene()
