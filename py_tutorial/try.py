#!/usr/bin/python3
# put your 'try by error' error code here 
try:
    prompt = 'Please enter the name of your favourite meal for breakfast:\n'
    inp = int(input(prompt))
    print(inp)
except ValueError:
                  print('Kindly enter only an integer next time')
finally:
        print('Thank you :)')
