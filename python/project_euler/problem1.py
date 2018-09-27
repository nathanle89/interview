def sumMultiple(upperbound):
    multiplier_of_three = upperbound / 3
    multiplier_of_five = upperbound / 5
    multiplier_of_fifteen = upperbound / 15

    sum = 0
    for i in range(1, multiplier_of_three + 1):
        if i <= multiplier_of_fifteen:
            sum -= 15*i
        if i < multiplier_of_five:
            sum += 3 * i + 5 * i
        else:
            sum += 3 * i

    return sum

print sumMultiple(1000)