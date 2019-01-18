n = int(input())
for i in range(0,n):
    largest_val = i

    k = 1
    while k <= largest_val:
        print(k, end='')
        k = k + 1

    k = largest_val+1
    while k >= 1:
        print(k, end='')
        k = k - 1

    print()

'''
n = int(input())
for i in range(0,n):
    largest_val = i
    has_passed_half = False

    k = 1
    while k > 0:
        suffix = ''
        if k == 1 
            suffix = '\n'
            
        print(k, end=suffix)

        if k >= largest_val+1:
            has_passed_half = True

        if has_passed_half:
            k = k - 1
        else:
            k = k + 1


'''