import time
from plotter import Plotter


goals = [10, 25, 20, 30, 15]
temp = 23
pltr = Plotter()
dt = 0.01
if __name__ == "__main__":
	for goal in goals:
		for i in range(int(1/dt)):
			pltr.draw(temp, goal)
			time.sleep(dt)
else:
	print("CACA")
