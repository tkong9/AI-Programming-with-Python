## Your code should check if each number in the list is a prime number
check_prime = [7, 9, 26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for num in check_prime:
    for i in range(2, num):
        if num % i == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
        if i == num - 1:
            print("{} IS a prime number".format(num))