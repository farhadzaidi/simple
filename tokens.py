DIGITS = '0123456789.'

T_INT = 'INT'
T_FLOAT = 'FLOAT'
T_PLUS = 'PLUS'
T_MINUS = 'MINUS'
T_MULT = 'MULT'
T_DIV = 'DIV'
T_INT_DIV = 'INT_DIV'
T_MOD = 'MOD'
T_POW = 'POW'
T_LPAREN = '('
T_RPAREN = ')'

class Token:
	def __init__(self, t_type, val=None):
		self.t_type = t_type
		self.val = val

	def __repr__(self):
		if self.val:
			return f'{self.t_type}:{self.val}'
		else:
			return f'{self.t_type}' 