from stack import Stack

class Main:
	stack_obj = Stack()

	quotient = int(input("Decimal:")) 
	divisor = 2  # here this value acts as base  
	converted_binary = []
	
	while quotient > divisor:
		remainder = quotient % divisor
		quotient = quotient / divisor
		stack_obj.push(int(remainder))
		if quotient < divisor:
			stack_obj.push(int(quotient))
	while not stack_obj.is_empty():
			removed_item = stack_obj.pop()
			converted_binary.append(removed_item) 
	print(f"Binary{converted_binary}")	
	