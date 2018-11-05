
import math

print('Quadratic Factoring Calculator (WIP)')
print('By Matthew Le Huenen')
print('ax^2 + bx + c')
print('-----------------------------------------------')
# There's probably some redundant code in here and a bunch of stuff that could be improved
inputed_quad = ''
output = ''

print('(If partially factored is the same as input, there is no common (numeric) denominator)\n')

while True: # Ensures that only integers are inputed
    try:
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))
        break

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


g_c_denom = math.gcd(math.gcd(a, b), c) # Checks if there is a greatest common denominator, if so factor it out

if a < 0:
    g_c_denom = g_c_denom*-1

if g_c_denom == 1:
    pf_output = ''
elif g_c_denom == -1:
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

print('Partially Factored: ', pf_output) # Print partially factored quad
print('')

discriminant = (b**2 - (4*a*c))

if discriminant < 0:
    output = "Cannot be Factored (no real roots)"

elif discriminant == 0: # Checks if it is a perfect square
    if math.sqrt(abs(a)).is_integer() and math.sqrt(abs(c)).is_integer: # Perfect square checks pt. 2, are all these checks even necessary?
        if ((int(math.sqrt(abs(a))))*(int(math.sqrt(abs(c)))))*2 == b or ((int(math.sqrt(abs(a))))*(int(math.sqrt(abs(c)))))*2 == b*-1: # Perfect Square checks pt. 3, better safe than sorry

            print("Perfect Square!")

            if g_c_denom == 1: # Build the factored perfect square
                output = '('
            elif g_c_denom == -1:
                output = '-('
            else:
                output = str(g_c_denom) + '('

            if a == 1 or a == -1:
                output = output + 'x'
            else:
                output = output + str(int(math.sqrt(a))) + 'x'

            if b < 0:
                output = output + ' – '
            else:
                output = output + ' + '

            output = output + str(int(math.sqrt(c))) + ')^2'

elif a > 0 and c < 0: # Checks for difference of squares
    if math.sqrt(a).is_integer() and math.sqrt(abs(c)).is_integer and b == 0: # Check pt. 2

        print("Difference of Squares!")

        if g_c_denom == 1: # Build the difference of squares
            output = '('
        elif g_c_denom == -1:
            output = '-('
        else:
            output = str(g_c_denom) + '('

        if int(math.sqrt(a)) == 1:
            output = output + 'x + ' + str(int(math.sqrt(abs(c)))) + ')(' + 'x – ' + str(int(math.sqrt(abs(c)))) + ')'
        else:
            output = output + str(int(math.sqrt(a))) + 'x + ' + str(int(math.sqrt(abs(c)))) + ')(' + str(int(math.sqrt(a))) + 'x – ' + str(int(math.sqrt(abs(c)))) + ')'

print(output + '\n')