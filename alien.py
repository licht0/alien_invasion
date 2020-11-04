import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""初始化外星人并设置其初始位置"""
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_setting = ai_settings
		
		#加载外星人图像,设置rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#设置外星人初始位置为左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#允许外星人x坐标为小数
		self.x = float(self.rect.x)

	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image, self.rect)
