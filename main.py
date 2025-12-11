from arithmetic import add, subtract

def main():
    # Taking input from user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Arithmetic calculations
    addition = add(a, b)
    subtraction = subtract(a, b)

    print("\n--- Results ---")
    print("Addition:", addition)
    print("Subtraction:", subtraction)

if __name__ == "__main__":
    main()
