def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Деление на ноль")
        return None

def calculate(expression):
    expression = expression.replace('+', ' + ')
    expression = expression.replace('-', ' - ')
    expression = expression.replace('*', ' * ')
    expression = expression.replace('/', ' / ')
    parts = expression.split()
    
    if len(parts) == 3 and parts[1] in ['+', '-', '*', '/']:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        
        if operator == '+':
            result = plus(num1, num2)
        elif operator == '-':
            result = minus(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
            
        if result is not None:
            print(f"Результат: {result}")
    else:
        print("Неверный формат выражения")
if __name__ == "__main__":
    while True:
        user_input = input("Введите выражение:")
        if user_input.lower() == 'q':
            break
        calculate(user_input)