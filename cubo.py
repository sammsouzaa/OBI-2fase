n = int(input())
f1 = 0
f2 = 0
f3 = 0
f0 = 0

if(n>2):
    meio = 0
    meio = (n-2) * (n-2)
    f1 = meio * 6


if (n>=3):
    f2 = (n-2) * 12


else: f2 = 0

if (n >= 2): f3 = 8
else: f3 = 0

if(n >= 3):
    meio = 0
    meio = (n-2) * (n-2)
    f0 = meio * (n-2)
else: f0 = 0

print(f0)
print(f1)
print(f2)
print(f3)