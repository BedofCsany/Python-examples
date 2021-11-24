a = int(input("Kérek egy számot!  a=  "))
b = int(input("Kérek egy számot!  b=  "))
c = int(input("Kérek egy számot!  c=  "))

if a == b == c:
    print("Mindhárom szám ugyanannyi volt.")
            
elif a == b and a > c:
    print("Az a és b ugyanannyi és ők a legnagyobbak.")

elif a == c and a > b:
    print("Az a és c ugyanannyi és ők a legnagyobbak.")
    
elif b == c and b > a:
    print("Az b és c ugyanannyi és ők a legnagyobbak.")

elif a > b and a > c:
    print("Az a szám a legnyagyobb, ami " + str(a)) 
    
elif b > a and b > c:
    print("A b szám a legnyagyobb, ami " + str(b))
    
elif c > b and c > a:
    print("A c szám a legnyagyobb, ami " + str(c))
