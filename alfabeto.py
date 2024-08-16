a, b = list(map(int, input().split()))
eounao = True

lalieningena = input()
lmensagem = input()

for letra in lmensagem:

    if(letra not in lalieningena):
        eounao = False
        break

if(eounao):
    print("S")
else:
    print("N")