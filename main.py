def Calculate(a,b): # Calculates the greatest common divisor of two integers using the Euclidean algorithm
    while b != 0: # The algorithm runs in a loop as long as 'b' is not equal to zero. This is the condition for the Euclidean algorithm to continue iterating, as the GDC is found when this condition is no longer met.
        remainder = a % b # This calculates the remainder of the division of 'a' by 'b'.
        a = b # Updates the value of 'a' to be 'b'. This step prepares for the next iteration (if any) by moving the divisor to the dividend's place.
        b = remainder # Updates the value of 'b' to be the remainder calculated previously. This effectively reduces the problem size for the next iteration, helping find the GCD.
    return a # Once this loop ends (because 'b' has become zero) the function returns 'a' because once b becomes zero a should hold the GCD.


nums = [] # this list is for storing the numbers the user inputs

while len(nums) < 2: # this ensures that the loop will only end once nums gets 2 numbers to be used in Calculate
    if len(nums) == 0: # this is to check if its the first number needed from the user so a custom message can be given asking for a number
        user_input = input("please enter a whole number that is positive: ")
    else: # this is to check if its the second number needed from the user so a custom message can be given asking for another number
        user_input = input("please enter another whole number that is positive to find the GCD: ")

    try: # this is to check if user_input is an int
        value = int(user_input)
        if value > 0: # this makes sure that only positive numbers can go through
            nums.append(value) # through this while loop only positve whole numbers can be entered into nums as well as this it informs the user what is required if a wrong type of input is given
        else:
            print("please enter a positive integer")
    except ValueError: # this ensures that if ValueError occurs while int casting is attempted then it lets the user know to only enter whole numbers
        print("please enter a whole number not a decimal number, letters, other symbols or an empty input")


print(str(Calculate(nums[0],nums[1])) + " is the GCD of your given numbers " + str(nums[0]) + " and " + str(nums[1])) # this calls Calculate and prints result and tells you the two numbers it used
