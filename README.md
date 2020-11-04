# alien_invasion

alien_invasion.py
主程序
WHILE循环调用check_events()、ship.update()、gf.update_bullets、gf.update_screen()


settings.py
设置,包含Settings类
初始化控制游戏外观、飞船速度、子弹长度、宽度、颜色、速度、最大同时允许数


game_functions.py
游戏功能函数
1.check_events()
检测输入事件
2.check_keydown_events()
检测按键事件
3.check_keyup_events()
检测松开按键事件
4.update_screen()
绘制屏幕
5.fire_bullet()
发射子弹
6.update_bullets()
更新子弹位置,删除消失的子弹


ship.py
飞船,包含Ship类
update()
管理飞船位置
blitme()
绘制飞船


bullet.py
子弹,包含Bullet类
update()
更新子弹位置
draw_bullet()
绘制子弹