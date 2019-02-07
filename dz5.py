import os
for x in range(1,10):
    name = 'dir' + str(x)
    path = os.path.join(os.getcwd(),name)
    try:
        os.mkdir(path)
    except FileExistsError:
        print(name, 'уже существует')


list = os.listdir(os.getcwd())
for y in list:
    if os.path.isdir(y):
        print(y)



