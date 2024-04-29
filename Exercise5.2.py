def check_fermat(a, b, c, n):
    """Check if Fermat's Last Theorem is violated."""
    # Check if n is greater than 2
    if n > 2:
        # Calculate a^n + b^n and c^n
        left_side = a ** n + b ** n
        right_side = c ** n
        
        # Check if a^n + b^n = c^n
        if left_side == right_side:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work.")
    else:
        # If n is not greater than 2, print a message indicating the theorem does not apply
        print("Fermat's theorem applies only for n > 2.")

def get_user_input_and_check():
    """Prompt the user for values and check if Fermat's theorem is violated."""
    # Prompt the user for values and convert them to integers
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = int(input("Enter value for c: "))
    n = int(input("Enter value for n: "))
    
    # Call the check_fermat function with user inputs
    check_fermat(a, b, c, n)

# Call the function to prompt user inputs and check Fermat's theorem
get_user_input_and_check()
