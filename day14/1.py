from input import INPUT

SECONDS = 100
WIDTH = 101
HEIGHT = 103

h_even = HEIGHT % 2 == 0
w_even = WIDTH % 2 == 0

robot_map = [[0] * WIDTH for x in range(HEIGHT)]

def quadrant(q):
	a, b, c, d = 0, 0, 0, 0
	
	if q == 1:
		a = 0
		b = HEIGHT // 2
		c = 0
		d = WIDTH // 2
	elif q == 2:
		a = 0
		b = HEIGHT // 2
		c = WIDTH // 2 if w_even else WIDTH // 2 + 1
		d = WIDTH
	elif q == 3:
		a = HEIGHT // 2 if h_even else HEIGHT // 2 + 1
		b = HEIGHT
		c = 0
		d = WIDTH // 2
	elif q == 4:
		a = HEIGHT // 2 if h_even else HEIGHT // 2 + 1
		b = HEIGHT
		c = WIDTH // 2 if w_even else WIDTH // 2 + 1
		d = WIDTH

	robots = 0
	for i in range(a, b):
		for j in range(c, d):
			robots += robot_map[i][j]
	return robots

def safety_factor():
	return quadrant(1) * quadrant(2) * quadrant(3) * quadrant(4)

def position_after_n_seconds(p: tuple[int, int], v: tuple[int, int], n):
	x_offset = (p[0] + v[0] * n) % WIDTH
	y_offset = (p[1] + v[1] * n) % HEIGHT
	x_offset = x_offset if x_offset >= 0 else WIDTH + x_offset
	y_offset = y_offset if y_offset >= 0 else HEIGHT + y_offset
	return y_offset, x_offset

def main():
	for robot in INPUT:
		position = position_after_n_seconds(robot["p"], robot["v"], SECONDS)
		robot_map[position[0]][position[1]] += 1
	print(safety_factor())

if __name__ == "__main__":
	main()
