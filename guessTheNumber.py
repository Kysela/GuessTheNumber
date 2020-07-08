import random
attempts = 0
n = random.randint(0,10000)
origin = n
while 1:
 randomChange = random.randint(0,100)
 operator = random.randint(0,1)
 value = input()
 if (value != n):
    attempts += 1
    print("Wrong number, try again...")
    if (operator == 0 and n-randomChange >= 0):
        n = n-randomChange
    elif (operator == 1 and n+randomChange <= 1000):
        n = n+randomChange
    if (n > value):
       print("May be go higher boi")
    else:
       print("May be go lower boi")
 else:
    print("Right number, congrats!!")
    print("Number of attempts is: " + str(attempts) + "!")
    print("Original number is " + str(origin) + "!")
    break

