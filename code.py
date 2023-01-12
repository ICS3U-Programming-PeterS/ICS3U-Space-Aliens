#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Jan 2023
# This program is the "Space Aliens" game for the PyBadge.
# It uses the ugame and stage libraries to manage the graphics
# and input for the game.

import stage
import ugame


def game_scene():
    # get user input
    keys = ugame.buttons.get_pressed()

    # This function sets up and runs the main game scene.

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("pingpong_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(image_bank_background, 10, 8)

    # Create the ship sprite using image at index 5, with initial position
    # (72,57)
    ship = stage.Sprite(image_bank_sprites, 5, 72, 57)
    table = stage.Sprite(image_bank_sprites, 0, 0, 50)

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # Add the background and ship to the layers list
    game.layers = [ship, table] + [background]

    # Draw the background on the screen
    game.render_block()

    # Game Loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # code to move ship sprite and to rap it
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
            if ship.x > 160:
                ship.move(0, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
            if ship.x < 0:
                ship.move(155, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
            if ship.y < 0:
                ship.move(ship.x, 128)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            if ship.y > 128:
                ship.move(ship.x, 0)

        # input to make the sprite move
        # Redraw the sprites on the screen
        game.render_sprites([ship, table])
        # Pause the loop to achieve 60fps frame rate
        game.tick()


if __name__ == "__main__":
    game_scene()
