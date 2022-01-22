from tokens import *
import lexer
import parser
import interpreter

def verify(tokens):
	i = 0
	j = 1
	NON_UNARY_OPS = (T_MULT, T_DIV, T_POW, T_INT_DIV, T_MOD)
	while j < len(tokens):
		if str(tokens[i].val) in DIGITS and str(tokens[j].val) in DIGITS:
			return False

		if tokens[i].t_type in NON_UNARY_OPS and tokens[j].t_type in NON_UNARY_OPS:
			return False

		i += 1
		j += 1

	OPERATORS = (T_PLUS, T_MINUS, T_MULT, T_DIV, T_POW, T_INT_DIV, T_MOD)
	if tokens[-1].t_type in OPERATORS:
		return False


	return True

def main():
	print('Simple')
	print("Input 'exit' to exit shell.")

	symbol_table = {}
	while True:
		string = input('>> ').strip()
		if string == '':
			continue
		elif string == 'exit':
			break
		else:
			new_lexer = lexer.Lexer(string)
			tokens = new_lexer.tokenize()
			
			if isinstance(tokens, list):
				verified = verify(tokens)
				if not verified:
					print('Syntax Error')
				else:
					new_parser = parser.Parser(tokens)
					ast = new_parser.parse()
					
					new_interpreter = interpreter.Interpreter(ast, symbol_table)
					result = new_interpreter.interpret()

					if result:
						print(result)


if __name__ == '__main__':
	main()
