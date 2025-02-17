a = input()
l = 0 
u = 0
k = 0
renge = 0
itog1 = ""
itog2 = ""
while a.find("#") == -1:
    k = 0
    if a.find("for") != -1:
        
        a = a[a.find("(")+ 1]
        renge = int(a)
        a = input()
        if a.find("    ") != -1:
            if a.find("right") != -1:
                l = l - 1*renge
            elif a.find("left") != -1:
                l = l + 1*renge
            elif a.find("up") != -1:
                u = u + 1*renge
            elif a.find("down") != -1:
                u = u - 1*renge
            else:
                a = input()
        
    else:
        
        if a.find("right") != -1:
            l = l - 1
        elif a.find("left") != -1:
            l = l + 1
        elif a.find("up") != -1:
            u = u + 1
        elif a.find("down") != -1:
            u = u - 1