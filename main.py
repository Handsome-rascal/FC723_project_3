def Calculate(a,b): # Calculates the greatest common divisor of two integers using the Euclidean algorithm
    while b != 0: # The algorithm runs in a loop as long as 'b' is not equal to zero. This is the condition for the Euclidean algorithm to continue iterating, as the GDC is found when this condition is no longer met.
        remainder = a % b # This calculates the remainder of the division of 'a' by 'b'.
        a = b # Updates the value of 'a' to be 'b'. This step prepares for the next iteration (if any) by moving the divisor to the dividend's place.
        b = remainder # Updates the value of 'b' to be the remainder calculated previously. This effectively reduces the problem size for the next iteration, helping find the GCD.
    return a # Once this loop ends (because 'b' has become zero) the function returns 'a' because once b becomes zero a should hold the GCD.
