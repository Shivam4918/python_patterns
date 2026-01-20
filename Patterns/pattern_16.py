count = 1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(count, end=" ")
#         count += 1
#     print()

def pattern1(n):
    count = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(count, end=" ")
            count += 1
        print()
pattern1(5)