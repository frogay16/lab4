def happy(tic):
    s1=0
    s2=0
    a = len(tic)
    if a%2==0:
        for i in range(0, a//2):
            s1 = s1+int(tic[0])
            tic = tic[1:]
        for i in range(a // 2, a):
            s2 = s2+int(tic[0])
            tic = tic[1:]
    else:
        return "Введите билет с четным количеством знаков."
    if s1==s2:
        return "Это счастливый билет!"
    return "Этот билет не является счастливым."

tic = str(input())
print(happy(tic))
