weight=int(input("weight : "))
unit=input('(L)bs or (K)g:')

if unit.upper()=="L":
    print(f"you are {weight*0.45}kilos")
else:
    print(f"you are {weight//0.45} pounds")
    