class Settings():
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# 飞船设置
		self.ship_speed_factor = 1

		# 子弹设置
		self.bullet_width = 3
		self.bullet_height = 10
		self.bullet_color = (0, 0, 0)
		self.bullet_speed_factor = 1.6
		self.bullets_allowed = 2