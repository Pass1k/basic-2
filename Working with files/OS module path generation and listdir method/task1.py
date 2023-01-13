import os

real_path = os.path.join("access", "admin.bat")
abs_path = os.path.abspath(real_path)

print('Абсолютный путь до файла:', abs_path)
print('Относительный путь до файла:', real_path)

