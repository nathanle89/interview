def sumSquareDiff():
    square_sum = 0
    sum_square = 0

    for i in range(1, 101):
        sum_square += i**2
        square_sum += i

    return square_sum**2 - sum_square

def theNthPrime(n):
    upperbound = 10000000
    prime_list = [True] * upperbound
    prime_list[0] = False
    prime_list[1] = False

    for i in range(2, int(upperbound**0.5)+1):
        if prime_list[i] == True:
            start_val = i
            while start_val < upperbound:
                start_val = start_val + i
                if start_val <= len(prime_list) - 1:
                    prime_list[start_val] = False

    counter = 0
    result = -1
    for i in range(0, len(prime_list)):
        if prime_list[i] == True:
            counter += 1
        if counter == n:
            result = i
            break

    return result

print theNthPrime(10001)
print sumSquareDiff()