["num1, num2, operation"]


def perform_operation(num1, num2, operation):

    if operation == "divide" and num2 == 0:
        return "can not divide by zero"

    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num1
        case "divide":
            return num1 / num2
        case _:
            return "please provide a valid operation"
