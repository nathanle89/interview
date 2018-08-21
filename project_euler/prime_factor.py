def largestPrimeFactor(input):
    result = -1

    # Keep dividing input by 2
    while input % 2 == 0:
        result = 2
        input /= 2

    # Keep dividing by odd number until the sqrt of input
    # Because that is the largest possible prime number
    for i in range(3, int(input ** 0.5) + 1, 2):
        while input % i == 0:
            input /= i
            result = i

    if input > 2:
        result = input

    return result

print largestPrimeFactor(600851475143)