

def gradient( p1 , p2 ):
	if p1[0] == p2[0]:
		return True
	else:
		return (p2[1]-p1[1])/(p2[0]-p1[0])

def r_gradient(p1 , p2):
	if p1[1] == p2[1]:
		return True
	else:
		return (p1[0]-p2[0])/(p1[1]-p2[1])

def tri_peak(circ,gradient,lenght, mouse):
	if gradient == True or circ == mouse:
		if mouse[1] <= circ[1]:
			return (circ[0] , circ[1] - lenght)
		else:
			return (circ[0] , circ[1] + lenght)
	delta_x = lenght / (gradient**2 + 1)**(1/2)
	if mouse[0] > circ[0]:
		return (circ[0] + delta_x, circ[1] + gradient * delta_x)
	else:
		return (circ[0] - delta_x, circ[1] - gradient * delta_x)

def delta(point_1, point_2, lenght):
	m = gradient(point_1, point_2)
	if m == True or point_1 == point_2:
		if point_1[1] > point_2[1]:
			return lenght, 0
		return 0, lenght
	elif m == 0:
		if point_1[0] > point_2[0]:
			return -lenght, 0
		else:
			return lenght, 0
	else:
		if point_1[0] > point_2[0]:
			if point_1[1] > point_2[1]:
				delta_x = -lenght / (m**2 + 1)**(1/2)
				delta_y = -lenght / ((1/m)**2 + 1)**(1/2)
			else:
				delta_x = -lenght / (m**2 + 1)**(1/2)
				delta_y = lenght / ((1/m)**2 + 1)**(1/2)
		else:
			if point_1[1] > point_2[1]:
				delta_x = lenght / (m**2 + 1)**(1/2)
				delta_y = -lenght / ((1/m)**2 + 1)**(1/2)
			else:
				delta_x = lenght / (m**2 + 1)**(1/2)
				delta_y = lenght / ((1/m)**2 + 1)**(1/2)
	return delta_x, delta_y

def dist(point_1,point_2,lenght):
	x = point_1[0] - point_2[0]
	y = point_1[1] - point_2[1]
	if lenght > (x ** 2 + y ** 2) ** (1/2):
		return True
	return False
