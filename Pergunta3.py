# 3) Descubra a lógica e complete o próximo elemento:

print("=-="*20)
#a
num = 1
print("="*20)
print(num)
while num < 9:
    num += 2
    print(num)

#b
print("="*20)
num2 = 1
while num2 < 128:
    num2 =num2 * 2
    print(num2)

#c
print(6**2 + 1)

#d
n = 8
print('-='*25)
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {} '.format(t3), end='')
    t1 = t2 
    t2 = t3
    cont += 1

#e
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

#f não consegui representar