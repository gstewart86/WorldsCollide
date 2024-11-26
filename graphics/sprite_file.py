from graphics.sprite import Sprite


class SpriteFile(Sprite):
    def __init__(self, path, palette):
        self.path = path
        super().__init__([], palette)

        with open(path, "rb") as input_file:
            self.data = list(input_file.read())
