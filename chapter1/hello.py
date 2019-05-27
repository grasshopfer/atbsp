#! python3

# obligatory "Hello world!" program

print('Hello world!')

print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is ' + str(len(myName)) + ' characters.')
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
