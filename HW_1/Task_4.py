# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

a = int(input("Введите количество долек в ширине шоколадки: "))
b = int(input("Введите количество долек в длине шоколадки: "))
c = int(input("Введите количество долек, которые нужно отломить: "))
if c<a*b and ((c%a==0) or (c%b==0)):
    print("YES")
else:
    print("NO")
