class Value:
	def __init__(self, data, _children=(), _op=''):
		self.data = data
		self.grad = 0
		self._backward = lambda: None
		self._prev = set(_children)
		self._op = _op
	def __repr__(self):
		return f"Value(data={self.data}, grad={int(self.grad)})"

	def __add__(self, other):
		 # Implement addition here
		out= Value(self.data + other.data, (self, other), '+')

		def _backward():
			self.grad+=out.grad
			other.grad+=out.grad
		out._backward=_backward
		return out

	def __mul__(self, other):
		# Implement multiplication here
		out=Value(self.data * other.data, (self, other), '*')

		def _backward():
			self.grad+=other.data * out.grad
			other.grad+=self.data * out.grad
		out._backward=_backward
		return out

	def relu(self):
		# Implement ReLU here
		x=self.data
		rl=max(0, x)
		out=Value(rl, (self, ), 'relu')

		def _backward():
			def d_dx_relu(y):
				if y<0:
					return 0
				else:
					return 1
			self.grad+=d_dx_relu(rl) * out.grad
		out._backward=_backward
		return out
	