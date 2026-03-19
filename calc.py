def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error: Cannot modulo by zero"
    return a % b

def calculator():
    print("=" * 40)
    print("   Python Calculator   ")
    print("=" * 40)
    print("Operations: +  -  *  /  %")
    print("Type 'exit' to quit")
    print("=" * 40)

    history = []

    while True:
        print()
        user_input = input("Enter expression (e.g. 5 + 3): ").strip()

        if user_input.lower() == 'exit':
            print("\nGoodbye!")
            break

        if user_input.lower() == 'history':
            if history:
                print("\n Calculation History:")
                for i, h in enumerate(history, 1):
                    print(f"  {i}. {h}")
            else:
                print("No history yet.")
            continue

        if user_input.lower() == 'clear':
            history.clear()
            print("History cleared.")
            continue

        
        parsed = None
        for op in ['+', '-', '*', '/', '%']
            parts = user_input.split(op)
            if len(parts) == 2:
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())
                    parsed = (a, op, b)
                    break
                except ValueError:
                    continue

        if parsed is None:
            print(" Invalid input. Please use format: number operator number")
            print("   Example: 10 + 5  or  8 * 3")
            continue

        a, op, b = parsed

        #calculation
        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
        elif op == '%':
            result = modulo(a, b)

       
        def fmt(n):
            return int(n) if isinstance(n, float) and n == int(n) else n

        if isinstance(result, str):  
            print(f"{result}")
        else:
            a_fmt = fmt(a)
            b_fmt = fmt(b)
            r_fmt = fmt(result)
            expression = f"{a_fmt} {op} {b_fmt} = {r_fmt}"
            print(f" {expression}")
            history.append(expression)

if __name__ == "__main__":
    calculator()
