class Number:
	def __init__(self, val):
		self.val = val

	def plus(self, other):
		if isinstance(other, Number):
			return Number(self.val + other.val)

	def minus(self, other):
		if isinstance(other, Number):
			return Number(self.val - other.val)

	def mult(self, other):
		if isinstance(other, Number):
			return Number(self.val * other.val)

	def div(self, other):
		if isinstance(other, Number):
			try:
				return Number(self.val / other.val)
			except ZeroDivisionError:
				print('Division by Zero Error')
				return None

	def int_div(self, other):
		if isinstance(other, Number):
			try:
				return Number(self.val // other.val)
			except ZeroDivisionError:
				print('Division by Zero Error')
				return None

	def mod(self, other):
		if isinstance(other, Number):
			try:
				return Number(self.val % other.val)
			except ZeroDivisionError:
				print('Division by Zero Error')
				return None

	def pow(self, other):
		if isinstance(other, Number):
			return Number(self.val**other.val)

	def ee(self, other):
		if isinstance(other, Number):
			return Number(int(self.val == other.val))

	def ne(self, other):
		if isinstance(other, Number):
			return Number(int(self.val != other.val))

	def gt(self, other):
		if isinstance(other, Number):
			return Number(int(self.val > other.val))

	def lt(self, other):
		if isinstance(other, Number):
			return Number(int(self.val < other.val))

	def gte(self, other):
		if isinstance(other, Number):
			return Number(int(self.val >= other.val))

	def lte(self, other):
		if isinstance(other, Number):
			return Number(int(self.val <= other.val))

	def and_(self, other):
		if isinstance(other, Number):
			return Number(int(self.val and other.val))	
	
	def or_(self, other):
		if isinstance(other, Number):
			return Number(int(self.val or other.val))	

	def not_(self):
		if self.val == 0:
			return Number(1)

		return Number(0)

	def __repr__(self):
		return f'{self.val}'