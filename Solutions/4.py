#A palindromic number reads the same both ways. The largest palindrome made from
#the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

product = 0
product_list = []

for i in range(100,1000):
    first_int = i
    for i in range(100,1000):
        second_int = i
        product = first_int * second_int
        product_list.append(product)

palindrome_list = []
for i in product_list:
    num = str(i)
    if len(num) > 5:
        if num[0] == num[5] and num[1] == num[4] and num[2] == num[3]:
            palindrome_list.append(num)

largest = 0
for i in palindrome_list:
    if int(i) > largest:
        largest = int(i)

print(largest)
