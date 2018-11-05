import math

print('Quadratic Factoring Calculator (WIP)')
print('ax^2 + bx + c')
print('-----------------------------------------------')

inputed_quad = ''

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
print('Input:', inputed_quad) # Print 

if (a > 0 and c > 0) or (a < 0 and c < 0): # Checks if it is a perfect square
    if math.sqrt(abs(a)).is_integer() and math.sqrt(abs(c)).is_integer: # Perfect square checks pt. 2
        if ((int(math.sqrt(abs(a))))*(int(math.sqrt(abs(c)))))*2 == b or ((int(math.sqrt(abs(a))))*(int(math.sqrt(abs(c)))))*2 == b*-1: # Perfect Square checks pt. 3

            print('')
            print("Perfect Square!")
            
            if (a > 0 and c > 0): # Build the factored perfect square
                output = '('

                if a == 1 or a == -1:
                    output = output + 'x'
                else:
                    output = output + str(int(math.sqrt(a))) + 'x'

                if b < 0:
                    output = output + ' – '
                else:
                    output = output + ' + '

                output = output + str(int(math.sqrt(c))) + ')^2'

            else:
                output = '-('

                if a == 1 or a == -1:
                    output = output + 'x'
                else:
                    output = output + str(int(math.sqrt(abs(a)))) + 'x'

                if b > 0:
                    output = output + ' – '
                else:
                    output = output + ' + '

                output = output + str(int(math.sqrt(abs(c)))) + ')^2'
    
print(output)