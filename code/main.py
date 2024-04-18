from os.path import join

from pytmx import TiledMap  # type: ignore
from pytmx.util_pygame import load_pygame  # type: ignore
from settings import *
from sprites import Sprite


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Monster Hunter")

        # groups
        self.all_sprites: pygame.sprite.Group[pygame.sprite.Sprite] = (
            pygame.sprite.Group()
        )

        self.import_assets()
        self.setup(self.tmx_maps["world"], "house")

    def import_assets(self) -> None:
        self.tmx_maps: dict[str, TiledMap] = {
            "world": load_pygame(join("data", "maps", "world.tmx"))
        }

    def setup(self, tmx_map: TiledMap, player_start_pos: str) -> None:
        for x, y, surf in tmx_map.get_layer_by_name("Terrain").tiles():  # type: ignore
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

    def run(self) -> None:
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # game logic
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
