from string import ascii_letters

DIGITS = '0123456789.'
LETTERS = ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

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
T_KEYWORD = 'KEYWORD'
T_IDENTIFIER = 'IDENITIFIER'
T_EQ = 'EQ'
T_EE = 'EE'
T_NE = 'NE'
T_GT = 'GT'
T_LT = 'LT'
T_GTE = 'GTE'
T_LTE = 'LTE'

KEYWORDS = [
	'var',
	'and',
	'or',
	'not',
]

class Token:
	def __init__(self, t_type, val=None):
		self.t_type = t_type
		self.val = val

	def matches(self, other):
		if self.t_type == other.t_type and self.val == other.val:
			return True

		return False

	def __repr__(self):
		if self.val:
			return f'{self.t_type}:{self.val}'
		else:
			return f'{self.t_type}' 