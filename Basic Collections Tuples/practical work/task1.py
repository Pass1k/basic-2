students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def function(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt

age1 = function(students)[1]
my_lst1 = function(students)[0]

id = []
age = []
for i in students:
    id.append(i)
    age.append(students[i]['age'])


print('Список пар "ID студента — возраст":', list(zip(id, age)))
print('Полный список интересов всех студентов:', set(my_lst1))
print('Общая длина всех фамилий студентов:', age1)




