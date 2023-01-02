import os


file = './large_dummy.txt'
if os.path.isfile(file):
    with open(file) as f:
        data = f.read()
        # print(data)
else:
    print('file not exist')