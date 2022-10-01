import os


file = './camera_history.txt'
if os.path.isfile(file):
    with open(file) as f:
        data = f.read()
        # print(data)
    with open(file, mode='a') as f:
        f.write('fuck kenkyu\n')
else:
    print('file not exist')