# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         print(j,end="")
#     print()

def pattern5(n):
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            print(j,end="")
        print()
pattern5(5)