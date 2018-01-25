#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
#see that the 6th prime is 13.
#What is the 10 001st prime number?

prime_point = int(input('How many prime numbers do you want to find?'))
prime_list = []

for prime in range(10,prime_point + 1):
    counter = 0
    for i in range(prime,1,-1):
        if prime % i != 0:
            counter += 1
            if counter == prime:
                prime_list.append(prime)

print(prime_list)
