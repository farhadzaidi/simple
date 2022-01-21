import lexer
import parser
import interpreter

def main():
	print('Simple')
	print("Input 'exit' to exit shell.")

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
				new_parser = parser.Parser(tokens)
				ast = new_parser.parse()

				# print(ast)
				new_interpreter = interpreter.Interpreter(ast)
				print(new_interpreter.interpret())

			else:
				print(tokens)


if __name__ == '__main__':
	main()