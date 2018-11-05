from math import gcd, sqrt
from fractions import Fraction

print('Quadratic Factorer')
print('By Matthew Le Huenen')
print('ax^2 + bx + c')
print('-----------------------------------------------')
# There's probably some redundant code in here and a bunch of stuff that could be improved

a = 0
b = 0
c = 0
inputed_quad = ''
output = '???'
try_again = ''

while try_again != 'n':

    try_again = ''

    while True: # Ensures that only integers are inputed
        try:
            a = int(input('a: '))
            b = int(input('b: '))
            c = int(input('c: '))
            break      # I could make a separate function to avoid using a while True, break thing, but I feel like that complicates it

        except ValueError:
            print('\nInvalid Input', '\n')


    if a != 0: # Builds the quad so the user can see what was inputed
        if a == 1:
            inputed_quad = 'x^2'
        elif a == -1:
            inputed_quad = '-x^2'
        else:
            inputed_quad = str(a) + 'x^2'

    if b != 0:
        if a != 0:
            if b < 0:
                inputed_quad = inputed_quad + ' – '
            else:
                inputed_quad = inputed_quad + ' + '

            if b == 1 or b == -1:
                inputed_quad = inputed_quad + 'x'
            else:
                inputed_quad = inputed_quad + str(abs(b)) + 'x'

        else:
            if b == 1:
                inputed_quad = inputed_quad + 'x'
            elif b == -1:
                inputed_quad = inputed_quad + '-x'
            else:
                inputed_quad = inputed_quad + str(b) + 'x'

    if c != 0:
        if b != 0 or a != 0:
            if c < 0:
                inputed_quad = inputed_quad + ' – '
            else:
                inputed_quad = inputed_quad + ' + '

            inputed_quad = inputed_quad + str(abs(c))

        else:
            inputed_quad = inputed_quad + str(c)

    print('')
    print('Input:', inputed_quad) # Print built quad


    g_c_denom = gcd(gcd(a, b), c) # Checks if there is a greatest common denominator, if so factor it out

    if a < 0:
        g_c_denom = g_c_denom*-1

    if (a != 0 and b == 0 and c == 0) or (a == 0 and b != 0 and c == 0) or (a == 0 and b == 0 and c != 0) or (g_c_denom == 1) or (a == 0 and b == 0 and c == 0): # Checks if quad can't be partially factored
        pass

    elif c == 0 and a != 0 and b != 0: # can but c = 0
        
        if g_c_denom == 1:
            pf_output = 'x('
        elif g_c_denom == -1:
            pf_output = '-x('
            a = a // g_c_denom
            b = b // g_c_denom
            c = c // g_c_denom
        else:
            pf_output = str(g_c_denom) + 'x('
            a = a // g_c_denom
            b = b // g_c_denom
            c = c // g_c_denom

        if a != 0: # Builds the quad again, this time partially factored (if it can be)
            if a == 1:
                pf_output = pf_output + 'x'
            elif a == -1:
                pf_output = pf_output + '-x'
            else:
                pf_output = pf_output + str(a) + 'x'

        if b != 0:
            if a != 0:
                if b < 0:
                    pf_output = pf_output + ' – '
                else:
                    pf_output = pf_output + ' + '

                pf_output = pf_output + str(abs(b))

            else:
                pf_output = pf_output + str(b)
                
        pf_output = pf_output + ')'
        print('Partially Factored: ', pf_output) # Print partially factored quad, with the x factored
        
    else:

        if g_c_denom == -1:
            pf_output = '-('
            a = a // g_c_denom
            b = b // g_c_denom
            c = c // g_c_denom
        else:
            pf_output = str(g_c_denom) + '('
            a = a // g_c_denom
            b = b // g_c_denom
            c = c // g_c_denom

        if a != 0: # Builds the quad again, this time partially factored (if it can be)
            if a == 1:
                pf_output = pf_output + 'x^2'
            elif a == -1:
                pf_output = pf_output + '-x^2'
            else:
                pf_output = pf_output + str(a) + 'x^2'

        if b != 0:
            if a != 0:
                if b < 0:
                    pf_output = pf_output + ' – '
                else:
                    pf_output = pf_output + ' + '

                if b == 1 or b == -1:
                    pf_output = pf_output + 'x'
                else:
                    pf_output = pf_output + str(abs(b)) + 'x'

            else:
                pf_output = pf_output + str(b) + 'x'

        if c != 0:
            if b != 0 or a != 0:
                if c < 0:
                    pf_output = pf_output + ' – '
                else:
                    pf_output = pf_output + ' + '

                pf_output = pf_output + str(abs(c))

            else:
                pf_output = pf_output + str(c)

        if g_c_denom != 1:
            pf_output = pf_output + ')'

        print('Partial Factor: ', pf_output) # Print partially factored quad

    discriminant = (b**2 - (4*a*c))

    if discriminant < 0:
        output = "\nCannot Factor (no real roots)"

    elif discriminant == 0 and ((a > 0 and c > 0) or (a < 0 and c < 0)): # Checks if it is a perfect square
        if sqrt(abs(a)).is_integer() and sqrt(abs(c)).is_integer(): # Perfect square checks pt. 2, are all these checks even necessary?
            if ((int(sqrt(abs(a))))*(int(sqrt(abs(c)))))*2 == b or ((int(sqrt(abs(a))))*(int(sqrt(abs(c)))))*2 == b*-1: # Perfect Square checks pt. 3, better safe than sorry

                print("\nPerfect Square:")

                if g_c_denom == 1: # Build the factored perfect square
                    output = '('
                elif g_c_denom == -1:
                    output = '-('
                else:
                    output = str(g_c_denom) + '('

                if a == 1 or a == -1:
                    output = output + 'x'
                else:
                    output = output + str(int(sqrt(a))) + 'x'

                if b < 0:
                    output = output + ' – '
                else:
                    output = output + ' + '

                output = output + str(int(sqrt(c))) + ')^2'

    elif a > 0 and c < 0 and sqrt(a).is_integer() and sqrt(abs(c)).is_integer() and b == 0: # Checks for difference of squares

        print("\nDifference of Squares:")

        if g_c_denom == 1: # Setup output
            output = '('
        elif g_c_denom == -1:
            output = '-('
        else:
            output = str(g_c_denom) + '('

        if int(sqrt(a)) == 1:
            output = output + 'x + ' + str(int(sqrt(abs(c)))) + ')(' + 'x – ' + str(int(sqrt(abs(c)))) + ')' # Build the difference of squares
        else:
            output = output + str(int(sqrt(a))) + 'x + ' + str(int(sqrt(abs(c)))) + ')(' + str(int(sqrt(a))) + 'x – ' + str(int(sqrt(abs(c)))) + ')'

    elif (a == 0 and b == 0 and c != 0) or (a != 0 and b == 0 and c == 0):
        output = "\nCannot Factor"

    elif (a == 0 and b == 0 and c == 0):
        output = "\nCannot Factor: No terms, what did you expect?"

    elif discriminant > 0 and sqrt(discriminant).is_integer(): # Checks if it is able to be factored
        if a != 0 and b != 0 and c != 0:
        
            print("\nFactored: ")

            root_1 = (-b + sqrt(discriminant))/(2*a) # Quadratic formula to calculate roots
            root_2 = (-b - sqrt(discriminant))/(2*a)

            intratio_1 = Fraction(root_1).limit_denominator()
            intratio_2 = Fraction(root_2).limit_denominator()

            fquad_1 = intratio_1.numerator
            fquad_2 = intratio_1.denominator
            fquad_3 = intratio_2.numerator
            fquad_4 = intratio_2.denominator

            if g_c_denom == 1: # Setup output
                output = '('
            elif g_c_denom == -1:
                output = '-('
            else:
                output = str(g_c_denom) + '('

            if fquad_2 == 1: # Build factored quad
                output = output + 'x'
            else:
                output = output + str(fquad_2) + 'x'

            if fquad_1 < 0:
                output = output + ' + ' + str(abs(fquad_1)) + ')('
            else:
                output = output + ' – ' + str(fquad_1) + ')('

            if fquad_4 == 1:
                output = output + 'x'
            else:
                output = output + str(fquad_4) + 'x'

            if fquad_3 < 0:
                output = output + ' + ' + str(abs(fquad_3)) + ')'
            else:
                output = output + ' – ' + str(fquad_3) + ')'

        else:
            output = "\nCannot Factor"

    else:
        output = "\nCannot Factor (irrational roots)"

    print(output + '\n')

    while try_again != 'n' and try_again != 'y':
        try_again = input("Run the program again? (Y/N): ")
        try_again.strip().lower()