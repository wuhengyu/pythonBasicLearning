def processs(string):
    print('Processing:', string)


# with open('diedai.txt') as f:
#     char = f.read(1)
#     while char:
#         processs(char)
#         char = f.read(1)


with open('diedai.txt') as f:
    while True:
        char = f.read(1)
        if not char:
            break
        processs(char)

