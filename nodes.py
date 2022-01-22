class NumNode:
	def __init__(self, node):
		self.node = node

	def __repr__(self):
		return f'{self.node}'

class UnaryOpNode:
	def __init__(self, op, node):
		self.op = op
		self.node = node

	def __repr__(self):
		return f'({self.op}, {self.node})'

class BinaryOpNode:
	def __init__(self, left_node, op, right_node):
		self.left_node = left_node
		self.op = op
		self.right_node = right_node

	def __repr__(self):
		return f'({self.left_node}, {self.op}, {self.right_node})'

class VarAccessNode:
	def __init__(self, id_token):
		self.id_token = id_token

	def __repr__(self):
		return f'{self.id_token}'

class VarAssignNode:
	def __init__(self, var_token, value_node):
		self.var_token = var_token
		self.value_node = value_node

	def __repr__(self):
		return f'({self.var_token}, {self.value_node.node})'
