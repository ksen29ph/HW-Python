#Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

print ("Введите общее количество журавликов: ")
n = int(input())
if n % 6 == 0:
    var = n//6
    print ("Петя сделал: ", var, "журавликов, Катя сделала: ", var*4, "журавликов, Сережа сделал: ", var, "журавликов") 