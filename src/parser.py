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

	def atom(self):
		if self.current_token:
			if self.current_token.t_type in (t.T_INT, t.T_FLOAT):
				token = self.current_token
				self.advance()
				return n.NumNode(token)

			elif self.current_token.t_type == t.T_IDENTIFIER:
				id_token = self.current_token
				self.advance()
				return n.VarAccessNode(id_token)

			elif self.current_token.t_type == t.T_LPAREN:
				self.advance()

				expr = self.expression()
				if self.current_token:
					if self.current_token.t_type == t.T_RPAREN:
						self.advance()
						return expr
				else:
					print("Syntax Error: expected ')'")

	def power(self):
		left_node = self.atom()

		while self.current_token and self.current_token.t_type == t.T_POW:
			op_token = self.current_token
			self.advance()
			right_node = self.factor()

			left_node = n.BinaryOpNode(left_node, op_token, right_node)

		return left_node		

	def factor(self):

		if self.current_token and self.current_token.t_type in (t.T_PLUS, t.T_MINUS):
			op_token = self.current_token
			self.advance()
			num = self.factor()
			return n.UnaryOpNode(op_token, num)

		return self.power()

	def term(self):
		left_node = self.factor()

		term_ops = (t.T_MULT, t.T_DIV, t.T_INT_DIV, t.T_MOD)
		while self.current_token and self.current_token.t_type in term_ops:
			op_token = self.current_token
			self.advance()
			right_node = self.factor()

			left_node = n.BinaryOpNode(left_node, op_token, right_node)

		return left_node

	def arith_expr(self):
		left_node = self.term()
		while self.current_token and self.current_token.t_type in (t.T_PLUS, t.T_MINUS):
			op_token = self.current_token
			self.advance()
			right_node = self.term()

			left_node = n.BinaryOpNode(left_node, op_token, right_node)

		return left_node

	def comp_expr(self):
		if self.current_token and self.current_token.matches(t.Token(t.T_KEYWORD, 'not')):
			self.advance()

			node = self.comp_expr()
			return n.UnaryOpNode(t.Token(t.T_KEYWORD, 'not'), node)

		left_node = self.arith_expr()
		comp_ops = (t.T_EE, t.T_NE, t.T_GT, t.T_LT, t.T_GTE, t.T_LTE)
		while self.current_token and self.current_token.t_type in comp_ops:
			op_token = self.current_token
			self.advance()
			right_node = self.arith_expr()

			left_node = n.BinaryOpNode(left_node, op_token, right_node)

		return left_node

	def expression(self):
		if self.current_token.matches(t.Token(t.T_KEYWORD, 'var')):
			self.advance()

			if self.current_token and self.current_token.t_type != t.T_IDENTIFIER:
				if self.current_token.val in t.KEYWORDS:
					keyword = self.current_token.val
					print(f"Syntax Error: cannot use keyword '{keyword}' as identifier")
				else:
					print('Syntax Error: expected identifier')
				return None

			var_token = self.current_token
			self.advance()

			if not self.current_token or self.current_token.t_type != t.T_EQ:
				print("Syntax Error: expected '='")
				return None

			self.advance()
			if self.current_token.val in t.KEYWORDS or self.current_token.t_type == t.T_EQ:
				print('Syntax Error: invalid expression')
				return None

			expr = self.expression()
			return n.VarAssignNode(var_token, expr)

		left_node = self.comp_expr()
		while self.current_token and (self.current_token.matches(t.Token(t.T_KEYWORD, 'and')) or self.current_token.matches(t.Token(t.T_KEYWORD, 'or'))):
			op_token = self.current_token
			self.advance()
			right_node = self.comp_expr()

			left_node = n.BinaryOpNode(left_node, op_token, right_node)

		return left_node

	def parse(self):
		return self.expression()