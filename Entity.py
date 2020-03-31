import pygame
import Game_Functions as Game
import sys
import random

class Entity:
	def __init__(self, screen, colour, point, radius):
		self.screen = screen
		self.colour = colour
		self.point = point
		self.radius = radius

	def draw_projectile(self):
			pygame.draw.circle(self.screen, self.colour, self.point, self.radius)
		
	def update_projectiles(self):
		self.point_true = (self.point_true[0] + self.delta_x,self.point_true[1] + self.delta_y)
		self.point = (int(self.point_true[0] + self.delta_x),int(self.point_true[1] + self.delta_y))

class player(Entity):
	def __init__(self, screen, colour, gun_colour, point, radius):
		super().__init__(screen, colour, point, radius)
		self.gun_colour = gun_colour

	def draw_player(self, mouse):
		slope = Game.gradient(self.point ,mouse)
		r_slope = Game.r_gradient(self.point,mouse)

		p1 = Game.tri_peak(self.point,slope,2.5 * self.radius, mouse)
		p2 = Game.tri_peak(self.point,-r_slope,self.radius, mouse)
		p3 = (2*self.point[0]-p2[0],2*self.point[1]-p2[1])
		pygame.draw.polygon(self.screen, self.gun_colour, [p1,p2,p3])
		pygame.draw.circle(self.screen, self.colour, self.point, self.radius)
		return (int(p1[0]),int(p1[1]))

	def update_player(self):
		pass

class projectile(Entity):
	count = 0
	def __init__(self, screen, colour, point, radius, start_point, ref_point, speed, max_bullets):
		super().__init__(screen, colour, point, radius)
		self.point_true = point
		self.speed = speed
		self.delta_x, self.delta_y = Game.delta(start_point, ref_point, speed)
		self.count = projectile.count
		projectile.count = (projectile.count + 1) % max_bullets



class enemy(Entity):
	count = 0
	def __init__(self, screen, colour, radius, ref_point, speed, width, height, max_enemy):
		super().__init__(screen, colour, ref_point, radius)
		x = random.choice([True,False])
		y = random.choice([True,False])
		r = random.random()
		if x + y:
			if not x:
				point = (r * width, -50)
			elif not y:
				point = (r * width, 50 + height)
			else:
				point = (-50 ,r * height)
				pass
		else:
			point = (50 + width, r * height)

		self.point = (int(point[0]),int(point[1]))
		self.point_true = point
		self.delta_x, self.delta_y = Game.delta(point,ref_point, speed)
		self.count = enemy.count
		enemy.count = (enemy.count + 1) % max_enemy

class boss(enemy):
	Boss_count = 0
	def __init__(self, screen, colour, radius, ref_point, speed, width, height, max_enemy):
		super().__init__(screen, colour, radius,ref_point, speed, width, height, max_enemy)
		self.hp = boss.Boss_count + 1
		boss.Boss_count += 1