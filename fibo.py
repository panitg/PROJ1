inp = int(input())

fib =[0,1]

def fibonacci(n):
	if n<0:
		print('invalid no')
	elif n<len(fib):
		return fib[n]
	else:
		temp_fin = fibonacci(n-1)+fibonacci(n-2)
		fib.append(temp_fib)
		return temp_fib


out=fibonacci(inp)
print(out)
