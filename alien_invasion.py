import pygame

import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien



def run_game():
	# 初始化游戏pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建一艘飞船
	ship = Ship(ai_settings, screen)

	# 创建一个用于存储子弹的编组
	bullets = Group()

	# 创建一个外星人
	alien = Alien(ai_settings, screen)

	# 开始游戏的主循环
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, alien, bullets)



run_game()