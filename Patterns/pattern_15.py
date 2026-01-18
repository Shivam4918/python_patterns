# for row in range(5,0,-1):
#     for column in range(row,0,-1):
#         print(column,end="")
#     print()

def pattern14(number):
    for row in range(5,0,-1):
        for column in range(row,0,-1):
            print(column,end="")
        print()
pattern14(5)