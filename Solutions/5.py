#2520 is the smallest number that can be divided by each of the numbers from
#1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the
#numbers from 1 to 20?

num_list = []
num_count = 0
numerator = 0
state = True
while state:
    num_count = 0
    numerator += 20
    print(numerator)
    for i in range(1,21):
        if numerator % i == 0:
            num_count += 1
            if num_count > 19:
                num_list.append(numerator)
                state = False
print('Solution:',num_list[0])
