import tokens as t
import nodes as n

# Parser
class Parser:
	def __init__(self, token_list):
		self.token_list = token_list
		self.index = 0
		self.current_token = token_list[0]

	def advance(self):
		self.index += 1
		if self.index >= len(self.token_list):
			self.current_token = None
		else:
			self.current_token = self.token_list[self.index]

	# creates NumNode for single ints or floats
	# evaluates expression inside parenthesis
	def atom(self):
		if self.current_token.t_type in (t.T_INT, t.T_FLOAT):
			token = self.current_token
			self.advance()
			return n.NumNode(token)

		elif self.current_token.t_type == t.T_LPAREN:
			self.advance()

			expr = self.expression()
			if self.current_token.t_type == t.T_RPAREN:
				self.advance()
				return expr

	# creates BinaryOpNode for atom (base) and factor (exponent) with '^' operator
	def power(self):
		left_node = self.atom()

		while self.current_token and self.current_token.t_type == t.T_POW:
			op_token = self.current_token
			self.advance()
			right_node = self.factor()

			left_node = n.BinaryOpNode(left_node, op_token, right_node)

		return left_node		

	# creates UnaryOpNode for factors and '+' or '-' operator
	def factor(self):

		if self.current_token.t_type in (t.T_PLUS, t.T_MINUS):
			op_token = self.current_token
			self.advance()
			num = self.factor()
			return n.UnaryOpNode(op_token, num)

		return self.power()


	# creates BinaryOpNode for 2 factors and mult/div operator
	def term(self):
		left_node = self.factor()

		term_ops = (t.T_MULT, t.T_DIV, t.T_INT_DIV, t.T_MOD)
		while self.current_token and self.current_token.t_type in term_ops:
			op_token = self.current_token
			self.advance()
			right_node = self.factor()

			left_node = n.BinaryOpNode(left_node, op_token, right_node)

		return left_node

	# creates BinaryOpNode for 2 terms and plus/minus operator
	def expression(self):
		left_node = self.term()

		while self.current_token and self.current_token.t_type in (t.T_PLUS, t.T_MINUS):
			op_token = self.current_token
			self.advance()
			right_node = self.term()

			left_node = n.BinaryOpNode(left_node, op_token, right_node)

		return left_node

	def parse(self):
		return self.expression()