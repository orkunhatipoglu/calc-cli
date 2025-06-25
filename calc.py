import sys

def calc(op, a, b):
	if op == "add": return a+b
	if op == "sub": return a-b
	if op == "mul": return a*b
	if op == "div": return a/b

if __name__=="__main__":
	if len(sys.argv)!=4:
		print("Usage: python3 calc.py [add|sub|mul|div] num1 num2")
	else:
		op=sys.argv[1]
		a=float(sys.argv[2])
		b=float(sys.argv[3])
		print(calc(op,a,b))
