def main():
    while True:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
        else:
            print("Please enter a positive integer size.")

    for _ in range(size):
        for _ in range(size):
            print("*", end="")
        print()


main()
