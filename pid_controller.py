

class PID_Controller():
	def __init__(self, k):
		self.last = 0
		self.current = 0
		self.kp, self.ki, self.kd = k
		
	def tick(self, data):
		self.current = data
		# TODO COSAS
		self.last = self.current
		return
		
	def P(self):
		
	def I(self):
	
	def D(self):
