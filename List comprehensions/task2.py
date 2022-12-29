text1 = input('Введите строку: ')
text2 = input('Введите дополнительный символ: ')

first_text = [x * 2 for x in text1]
second_text = [x * 2 + text2 for x in text1]

print('Список удвоенных символов:', first_text)
print('Склейка с дополнительным символом:', second_text)