from cmath import sqrt
from math import erfc
from pickletools import uint1, uint4
from uuid import uuid3
import mpmath

def Frequency_bit_test():
    bit128="" 
    with open("128.txt", mode="r") as file:
          bit128=file.read()
    sum=0
   # bit128='11110'
    for elem in bit128:
        if elem=='1':
            sum+=1    
        else:
            sum+=-1

    print(erfc(sum/16))

def identical_consecutive_bits():
    bit128="" 
    with open("128.txt", mode="r") as file:
          bit128=file.read()
    sum=0
    for elem in bit128:
        if elem=='1':
            sum+=1 
    grek_i=sum/128 
    if abs(grek_i-0.5)<(2/sqrt(128).real):
        V=0
        for i in  range(127):
            if bit128[i]!=bit128[i+1]:
                V+=1
        tmp=abs(V-256*grek_i*(1-grek_i)) /         (32*grek_i*(1-grek_i))
        print(erfc(tmp))
    else: print(0)

def long_one():
    bit128="" 
    with open("128.txt", mode="r") as file:
          bit128=file.read()
    bloks=[]
    for i in range(16):
        bloks.append(bit128[8*i:8*i+8])
    u=[0,0,0,0]
    for elem in bloks:
        i=0
        tmp_max=0
        max_1=0
        while i<len(elem):
            if elem[i]=="1":
                while  i<len(elem) and elem[i]=="1":
                    tmp_max+=1
                    i+=1
                if max_1<tmp_max: 
                    max_1=tmp_max
                tmp_max=0
            i+=1

        if max_1<=1:u[0]+=1
        elif max_1==2:u[1]+=1
        elif max_1==3:u[2]+=1
        else: u[3]+=1
    p=[0.2148,0.3672,0.2305,0.1875]

    xi_2=0
    for i in range (4):
        xi_2+=(u[i]-16*p[i])*(u[i]-16*p[i])/16*p[i]   
    print(mpmath.gammainc(1.5,0.5*xi_2))
    
def main():
    Frequency_bit_test()
    identical_consecutive_bits()
    long_one()


if __name__=="__main__":
    main()