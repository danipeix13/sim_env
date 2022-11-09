import matplotlib.pyplot as plt
from collections import deque
import numpy as np

class Plotter():
	def __init__(self):
		plt.ion()
		self.visible = 120
		self.temp_q = deque(np.zeros(self.visible), self.visible)
		self.goal_q = deque(np.zeros(self.visible), self.visible)
		self.dx = deque(np.zeros(self.visible), self.visible)
		self.data_length = np.linspace(0, 121, num=120)

		self.fig = plt.figure(figsize=(6, 3))
		self.ah1 = self.fig.add_subplot()
		plt.margins(x=0.001)
		self.ah1.set_ylabel("Temperature(ºC)", fontsize=14)
		self.temp_p, = self.ah1.plot(self.dx, self.temp_q, color='red', label="Current Temperature", linewidth=1.0)
		self.goal_p, = self.ah1.plot(self.dx, self.goal_q, color='blue', label="Goal Temperature", linewidth=1.0)

		self.ah1.legend(loc="upper right", fontsize=12, fancybox=True, framealpha=0.5)
		self.x_data = 0

	def draw(self, temp, goal):
		self.temp_q.extend([temp])
		self.goal_q.extend([goal])
		self.dx.extend([self.x_data])

		# update plot
		self.temp_p.set_ydata(self.temp_q)
		self.temp_p.set_xdata(self.dx)
		self.goal_p.set_ydata(self.goal_q)
		self.goal_p.set_xdata(self.dx)

		# set axes
		self.ah1.set_ylim(-50, 50)
		self.ah1.set_xlim(self.x_data-self.visible, self.x_data)

		# control speed of moving time-series
		self.x_data += 1

		self.fig.canvas.draw()
		self.fig.canvas.flush_events()
