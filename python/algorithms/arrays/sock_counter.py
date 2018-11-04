def sockMerchant(n, ar):

    if not ar:
        return 0

    socks_map = {}
    for i in range(n):
        if ar[i] in socks_map:
            socks_map[ar[i]] += 1
        else:
            socks_map[ar[i]] = 1

    sock_counter = 0
    for key, val in socks_map.iteritems():
        sock_counter += (val / 2)

    return sock_counter

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3,]))