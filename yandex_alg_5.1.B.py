a=input()
b=input()
isHomeOrAway=int(input())
f1=int(a[0])
f2=int(b[0])
s1=int(a[2])
s2=int(b[2])
if f1+f2>s1+s2 or (isHomeOrAway==2 and f1+f2==s1+s2 and f1>s2) or (isHomeOrAway==1 and f1+f2==s1+s2 and f2>s1):
    print(0)
    exit()
elif (f1+f2==s1+s2):
    print(1)
    exit()
elif (f1+f2<s1+s2 and isHomeOrAway==1 and f2>=s1):
    print(s1+s2-f1-f2)
    exit()
elif (f1+f2<s1+s2 and isHomeOrAway==1 and s1+s2-f1-f2==s2+s1):
    print(s1+s2-f1-f2)
    exit()
elif f1+f2<s1+s2 and isHomeOrAway==1 and s1+s2-f1>=s2:
    print(s1 + s2 - f1 - f2)
    exit()
elif f1+f2<s1+s2 and isHomeOrAway==2 and f1>s2:
    print(s1 + s2 - f1 - f2)
    exit()
else:
    print(s1+s2-f1-f2+1)

# 0:2
# 0:3
# 1


# 5:2
# 0:5
# 1      3
# 1 - дома