a, b = int(input()), int(input())

c = ((a % 10) + (b % 10)) % 10
d = ((a // 10 % 10) + (b // 10 % 10)) % 10
e = ((a // 100) + (b // 100)) % 10

print(f'{e}{d}{c}')
