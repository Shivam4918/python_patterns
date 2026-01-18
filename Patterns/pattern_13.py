# for row in range(1,6):
#     for column in range(6,row+0,-1):
#         print("*",end="")
#     print()

def pattern13(number):
    for row in range(1,6):
        for column in range(6,row+0,-1):
            print("*",end="")
        print()
pattern13(5)