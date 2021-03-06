#Each new term in the Fibonacci sequence is generated by adding the previous two
#terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed
#four million, find the sum of the even-valued terms.

def fib(upper):
    previous = 1
    current = 2
    # leading edge of computation
    edge = 0
    fib_sum = 0
    while current <= upper:
        edge = previous + current
        print(edge)
        previous = current
        current = edge
        if edge % 2 == 0:
            fib_sum += edge
    return fib_sum

try:
    upper = int(input('Enter an upper bound:'))
except:
    print('Error, enter an integer.')
    quit()

print("The sum of even-valued terms:",fib(upper)+2)
