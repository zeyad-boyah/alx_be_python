def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return 1
            else:
                result = num1 / num2
        case _:
            print("Invalid operation.")
            return 1

    print(f"The result is {result}")


main()
