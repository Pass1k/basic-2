import os

path = 'C:\\Users\\paras\\PycharmProjects\\basic-2\\Working with files'


def obxodFile(path, level=1):
    print('level=', level, 'content:', os.listdir(path))

    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            obxodFile(path + '\\' + i, level + 1)
            print('Возврощаемся в', path)


obxodFile(path)
