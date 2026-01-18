# for row in range(5,0,-1):
#     for column in range(row,0,-1):
#         print(row,end="")
#     print()

def pattern14(number):
    for row in range(5,0,-1):
        for column in range(row,0,-1):
            print(row,end="")
        print()
pattern14(5)