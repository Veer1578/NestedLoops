string = input('Enter your word ')
char = input('Enter  the character you wish to check ')
i = 0
count = 0

while i < len(string):
    if string[i] == char:
        count = count + 1
    i = i + 1

print(f'The total number of times {char} has occured in {string} is {count}.')
