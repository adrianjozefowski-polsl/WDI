while True:
    wybor=int(input('Wybierz konwerter:\n1-Z Fahrenheita Do Celsjusza \n0-Z Celsjusza Do Fahrenheita\n'))
    if wybor==1:
        f=int(input('podaj stopnie Fahrenheita:'))
        c=(f-32)/1.8
        print(c)
        break
    if wybor==0:
        c=int(input('Podaj stopnie Celsjusza:'))
        f=c*1.8+32
        print(f)
        break
    else:
        print('Błąd podaj liczbę 0 lub 1 \n')
input()