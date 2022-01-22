import tokens as t
import nodes as n

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

	def __repr__(self):
		return f'{self.val}'

class Interpreter:
	def __init__(self, node, symbol_table):
		self.node = node
		self.symbol_table = symbol_table

	def interpret(self):
		if isinstance(self.node, n.NumNode):
			return self.interpret_NumNode()
		elif isinstance(self.node, n.UnaryOpNode):
			return self.interpret_UnaryOpNode()
		elif isinstance(self.node, n.BinaryOpNode):
			return self.interpret_BinaryOpNode()
		elif isinstance(self.node, n.VarAccessNode):
			return self.interpret_VarAccessNode()
		elif isinstance(self.node, n.VarAssignNode):
			return self.interpret_VarAssignNode()

	def interpret_NumNode(self):
		return Number(self.node.node.val)

	def interpret_UnaryOpNode(self):
		op_token = self.node.op
		self.node = self.node.node
		num = self.interpret()

		if op_token.t_type == t.T_MINUS:
			return num.mult(Number(-1))

		return num

	def interpret_BinaryOpNode(self):
		left_node = self.node.left_node
		right_node = self.node.right_node
		op_token_type = self.node.op.t_type

		self.node = left_node
		left_num = self.interpret()
		self.node = right_node
		right_num = self.interpret()

		if not left_num or not right_num:
			return None

		if op_token_type == t.T_PLUS:
			return left_num.plus(right_num)
		elif op_token_type == t.T_MINUS:
			return left_num.minus(right_num)
		elif op_token_type == t.T_MULT:
			return left_num.mult(right_num)
		elif op_token_type == t.T_DIV:
			return left_num.div(right_num)
		elif op_token_type == t.T_INT_DIV:
			return left_num.int_div(right_num)
		elif op_token_type == t.T_MOD:
			return left_num.mod(right_num)
		elif op_token_type == t.T_POW:
			return left_num.pow(right_num)

	def interpret_VarAccessNode(self):
		var_name = self.node.id_token.val
		try:
			value = self.symbol_table[var_name]
		except KeyError:
			print(f"'{var_name}' is not defined.")
			return None

		return value

	def interpret_VarAssignNode(self):
		var_token = self.node.var_token
		self.node = self.node.value_node
		value_node = self.interpret()

		if value_node:
			self.symbol_table[var_token.val] = value_node


