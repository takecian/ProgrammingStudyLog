# https://paiza.jp/challenges/241/show

dog = 0
cat = 0
for i in range(3):
    s = input()
    if s == 'cat':
        cat += 1
    else:
        dog += 1

if cat > dog:
    print('cat')
else:
    print('dog')