def checkPalindrome(input):
    str_val = str(input)
    index_forward = 0
    index_backward = len(str_val) - 1
    while index_forward < index_backward:
        if str_val[index_forward] != str_val[index_backward]:
            return False
        index_forward += 1
        index_backward -= 1
    return True

def largestProductPalindrome():
    currentLargest = 1
    for i in reversed(range(100, 1000)):

        for j in reversed(range(100, i)):
            product = i * j
            if checkPalindrome(product) and product > currentLargest:
                currentLargest = product
    return currentLargest

print largestProductPalindrome()