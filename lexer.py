import tokens as t

class Lexer:
	def __init__(self, string):
		self.string = string
		self.index = 0
		self.current_char = string[0]

	def advance(self):
		self.index += 1
		if self.index >= len(self.string):
			self.current_char = None
		else:
			self.current_char = self.string[self.index]

	def tokenize_num(self):
		is_float = False
		num_str = ''
		while self.current_char and self.current_char in t.DIGITS:
			if self.current_char == '.':
				is_float = True

			num_str += self.current_char
			self.advance()

		try:
			if is_float:
				return t.Token(t.T_FLOAT, float(num_str))
			else:
				return t.Token(t.T_INT, int(num_str))
		except ValueError:
			print('Syntax Error')
			return None

	def tokenize(self):
		token_list = []

		while self.current_char:
			if self.current_char == ' ':
				self.advance()
			elif self.current_char in t.DIGITS:
				token_list.append(self.tokenize_num())
			elif self.current_char == '+':
				token_list.append(t.Token(t.T_PLUS))
				self.advance()
			elif self.current_char == '-':
				token_list.append(t.Token(t.T_MINUS))
				self.advance()
			elif self.current_char == '*':
				token_list.append(t.Token(t.T_MULT))
				self.advance()
			elif self.current_char == '/':
				if self.string[self.index+1] == '/':
					token_list.append(t.Token(t.T_INT_DIV))
					self.advance()
					self.advance()
				else:
					token_list.append(t.Token(t.T_DIV))
					self.advance()
			elif self.current_char == '%':
				token_list.append(t.Token(t.T_MOD))
				self.advance()
			elif self.current_char == '^':
				token_list.append(t.Token(t.T_POW))
				self.advance()
			elif self.current_char == '(':
				token_list.append(t.Token(t.T_LPAREN))
				self.advance()
			elif self.current_char == ')':
				token_list.append(t.Token(t.T_RPAREN))
				self.advance()
			else:
				print(f"Invalid Character: '{self.current_char}'")
				return None

		if None in token_list:
			return None

		return token_list
