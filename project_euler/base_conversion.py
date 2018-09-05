def convert(inputNum, fromBase, toBase):
    toNum = 0
    power = 0

    while inputNum > 0:
        toNum += fromBase ** power * (inputNum % toBase)
        power += 1
        inputNum //= toBase

    return toNum

print convert(1010, 2, 10)
print convert(8, 10, 2)