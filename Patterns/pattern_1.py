# for i in range(1,6):
#     for j in range(1,6):
#         print("* ",end="")
#     print()

def pattern1(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("* ",end="")
        print()

pattern1(5)