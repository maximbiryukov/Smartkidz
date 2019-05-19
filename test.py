import random

N = 20

upper = 1
lower = 20

results = {'правильные':0, 'неправильные':0}

for i in range(N):
    print('')
    a = random.randint(upper, lower)
    b = random.randint(upper, lower)
    c = a + b
    print("{} + {} = ".format(a, b), end = '')
    answer = int(input())
    print('')
    if answer == c:
        print('МОЛОДЕЦ!')
        results['правильные'] += 1
    else:
        print('НЕПРАВИЛЬНО!')
        results['неправильные'] += 1
print(' ')
print('Результаты:')
print('{} правильных и {} неправильных'.format(results['правильные'], results['неправильные']))

