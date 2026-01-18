# for row in range(69,64):
#     for column in range(69,64):
#         print(chr(row),end="")
#     print()

def pattern8(number):
    for row in range(69,64,-1):
        for column in range(69,64,-1):
            print(chr(row),end="")
        print()
pattern8(5)