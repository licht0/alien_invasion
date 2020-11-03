import sys

import pygame

from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
	"""开火"""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按下按键"""
	#向右移动飞船
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	#向左移动飞船
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	#发射子弹
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	#关闭游戏快捷键
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	"""响应松开按键"""
	#停止向右移动飞船
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	#停止向左移动飞船
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""响应键盘和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#退出游戏
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			#按下某个按键
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			#松开某个按键
			check_keyup_events(event, ship)

def update_bullets(bullets):
	"""更新子弹位置,删除已消失的子弹"""
	bullets.update()

	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, bullets):
	"""更新屏幕上的图像,并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	# 让最近绘制的屏幕可见
	pygame.display.flip()