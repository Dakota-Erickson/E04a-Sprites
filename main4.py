#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.blue_5)
        self.animal_list = arcade.SpriteList()


    def setup(self):
        self.animal_sprite = arcade.Sprite("assets/ship (1).png", 0.5)
        self.animal_sprite.center_x = 500
        self.animal_sprite.center_y = 50
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/ship (2).png", 0.5)
        self.animal_sprite.center_x = 500
        self.animal_sprite.center_y = 150
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/ship (3).png", 0.5)
        self.animal_sprite.center_x = 500
        self.animal_sprite.center_y = 250
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/ship (4).png", 0.5)
        self.animal_sprite.center_x = 500
        self.animal_sprite.center_y = 350
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/ship (5).png", 0.5)
        self.animal_sprite.center_x = 500
        self.animal_sprite.center_y = 450
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/ship (6).png", 0.5)
        self.animal_sprite.center_x = 200
        self.animal_sprite.center_y = 50
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/ship (7).png", 0.5)
        self.animal_sprite.center_x = 200
        self.animal_sprite.center_y = 150
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/ship (8).png", 0.5)
        self.animal_sprite.center_x = 200
        self.animal_sprite.center_y = 250
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/ship (9).png", 0.5)
        self.animal_sprite.center_x = 200
        self.animal_sprite.center_y = 350
        self.animal_list.append(self.animal_sprite)

        self.animal_sprite = arcade.Sprite("assets/ship (10).png", 0.5)
        self.animal_sprite.center_x = 200
        self.animal_sprite.center_y = 450
        self.animal_list.append(self.animal_sprite)

    def on_draw(self):
        arcade.start_render()
        self.animal_list.draw()



    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()