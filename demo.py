import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Example"
SPEED = 10


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.APPLE_GREEN)
        self.monkey = None
        self.move_sound = None

        self.banana_list = None
        self.num_banana = 0
        self.time = 0

    def setup(self):
        self.monkey = arcade.Sprite("images/monkey.png", scale=0.1,
                                    center_x=400, center_y=400)
        self.move_sound = arcade.load_sound("audio/move.wav")

        self.banana_list = arcade.SpriteList()
        for x in range(100, 400, 100):
            banana = arcade.Sprite("images/banana.png", scale=0.1,
                                   center_x=x, center_y=200)
            self.banana_list.append(banana)

    def on_draw(self):
        arcade.start_render()
        self.monkey.draw()
        self.banana_list.draw()
        self.eat = arcade.check_for_collision_with_list(self.monkey, self.banana_list)
        for banana in self.eat:
            self.banana_list.remove(banana)
            self.num_banana += 1

        # Messages
        num_banana = f"# of Bananas: {self.num_banana}"
        arcade.draw_text(num_banana, 600, 50, (255, 211, 0), 20)

    def on_update(self, time):
        self.monkey.update()
        self.time += time

    def on_key_press(self, key, mod):
        if key == arcade.key.LEFT:
            self.monkey.change_x = -SPEED
        elif key == arcade.key.RIGHT:
            self.monkey.change_x = +SPEED
        elif key == arcade.key.DOWN:
            self.monkey.change_y = -SPEED
        elif key == arcade.key.UP:
            self.monkey.change_y = +SPEED
            arcade.play_sound(self.move_sound)

    def on_key_release(self, key, mod):
        if key == arcade.key.LEFT:
            self.monkey.change_x = 0
        elif key == arcade.key.RIGHT:
            self.monkey.change_x = 0
        elif key == arcade.key.DOWN:
            self.monkey.change_y = 0
        elif key == arcade.key.UP:
            self.monkey.change_y = 0


def main():
    window = Game()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
