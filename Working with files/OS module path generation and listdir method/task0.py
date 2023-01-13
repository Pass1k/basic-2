import os

folder_name = 'project'
file_name = 'ANIME'


path = 'docs/{folder}/{file}'.format(
    folder=folder_name,
    file=file_name,
)

print(path)

real_path = os.path.join('docs', folder_name, file_name)

print(real_path)

abs_path = os.path.abspath(file_name)
