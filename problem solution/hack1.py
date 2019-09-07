from re import match,compile
mat-=compile('^[+-]?[0-9]*/.[0-9]+$')
for _ in range(int(input())):
    print(bool(mat.match(input())))
