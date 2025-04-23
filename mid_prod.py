num = int(input('Enter the number: '))
t = num
numLen = 0

# Calculate the number of digits
while t > 0:
    numLen += 1
    t //= 10

if numLen >= 4:
    midIndex1 = numLen // 2
    chk = 0
    mid1 = mid2 = 0

    while num > 0:
        rem = num % 10

        if numLen % 2 == 0:
            if chk == midIndex1:
                mid1 = rem
            elif chk == (midIndex1 - 1):
                mid2 = rem
        else:
            if chk == midIndex1:
                mid1 = rem

        num //= 10
        chk += 1

    # Move print block here, after digit processing
    if numLen % 2 == 0:
        prod = mid1 * mid2
        print(f'The product of middle digits is ({mid1} * {mid2}) = {prod}')
    else:
        print(f'The product of middle digit is {mid1}')
else:
    print('It is not a 4 digit or less than 4 digit number.')
