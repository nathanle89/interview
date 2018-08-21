def sumEvenFib(upperbound):
    sum = 0
    current_val = 1
    previous_val = 1

    while current_val < upperbound:
        next_val = current_val + previous_val
        previous_val = current_val
        current_val = next_val

        if current_val % 2 == 0:
            sum += current_val
    return sum

print sumEvenFib(4000000)