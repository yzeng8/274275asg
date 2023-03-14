"""
Make sure your passwordvalidate.py is in the same folder as this tool,
and the file/function names must match assignment instructions.

Uncomment functions at the bottom of this document, save, then run this program in
your terminal.

Let me know if you are having difficulty.

- Braeden Provost, bprovost@ualberta.ca
"""

from passwordvalidate import *
from random import randint

# Checks your validate function against the given assignment inputs
def validate_check():

    #input1 = [x for x in input('Paste text from input_quoted.txt: ').split('"')]
    #output1 = [x for x in input('Paste text from output_spaced.txt: ').split()]
    inputfile = open('input_quoted', 'r')
    inputread = inputfile.read()
    input1 = [x for x in inputread.split('"')]
    outputfile = open('output_spaced', 'r')
    outputread = outputfile.read()
    output1 = [x for x in outputread.split()]
    index = 0
    index_to_fix = []

    for inp in input1:

        if validate(inp) == output1[index]:
            index += 1
            continue

        else:
            index_to_fix.append(index)
            index += 1

    if len(index_to_fix) > 0:
        for fixind in index_to_fix:

            print(
            'The password {} did not return {}'.format(input1[fixind],
             output1[fixind])
             )

    else: print('The validate function has passed the given test. Congrats!')


# Generates a number (n) of random passwords using generate function, then tests to make sure they are secure
def generate_check(n):

    verification = 0

    for num in range(n):

        # If you want to test a specific password length, replace 'randint(8,20)' with your desired number 
        pass_check = validate(generate(randint(8,20)))

        if pass_check != 'Secure':
            verification = 1
            print('A password has not returned SECURE, adjust function.')
            break

        else:
            continue

    if verification == 0:
        print('The test has not revealed any faults')


testcase = int(input('What function should be tested? Enter 1 for validate(), or 2 for generate()'))
if testcase == 1:
    validate_check()

elif testcase == 2:
    generate_check(int(input('How many passwords would you like to generate?: ')))

else:
    print('Invalid response.')