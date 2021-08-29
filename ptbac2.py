from math import *
print('Giải phương trình ax^2+bx+c=0')
a= int(input('Nhập số a: '))
b= int(input('Nhập số b: '))
c= int(input('Nhập số c: '))
print(f'Ta cần giải phương trình {a}x^2+{b}x+{c}=0')
delta = b*b-4*a*c
if delta <0:
    x1=complex((-b)/(2*a),sqrt(abs(delta))/(2*a))
    x2=complex((-b)/(2*a),-sqrt(abs(delta))/(2*a))
    print('Phương trình có hai nghiệm phức : x1=',x1, ',x2=',x2)
elif delta == 0:
    x= (-b)/(2*a)
    print('Phương trình nghiệm kép: x=', x)
else:
    x1=((-b)+sqrt(delta))/2*a
    x2=((-b)-sqrt(delta))/2*a
    print('Phương trình có hai nghiệm phân biệt: x1=',x1,',x2=',x2)