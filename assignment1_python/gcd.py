def gcd(x,y):

    def calculate_gcd(x,y):
        while y:
            x,y=y,x%y
            return x

    #Checking if the x and y are numbers  
    while True:
        try:
            print "Validating x" 
            int(x)
            print "x is valid"
        except ValueError:
            print "Invalid value of x"
            raise
            break
        try:
            print "Validating y"
            int(y)
            print "y is valid"
        except ValueError:
            print "Invalid value of y"
            raise
            break

        # Checking if x and y are negative numbers
        if x < 0 or  y < 0:
            raise ValueError, "Oops, I got a negative number here. You gotta give me a positive number"

        # Checking if the number is of type 'long'
        if type(x) != long or type(y) != long:
            raise TypeError, "Are you sure you gave me a 'long' number? :("    
 
        print "Let's calculate gcd"
        print "gcd is",calculate_gcd(x,y)
        break
