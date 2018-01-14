#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

calculated = 1
factor_list = []
limit = int(input('Enter a number:'))
i = 1
for i in range(1,limit):
    if calculated >= limit:
        break
    elif limit % i == 0:
        factor_list.append(i)
        calculated = calculated * i

print(factor_list)
