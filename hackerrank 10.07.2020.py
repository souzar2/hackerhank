#!/bin/python3

#print Hello, World!
def Hello():
	print("Hello, World!")


#if_else
def if_else(n):
    if n%2!=0 or n>=6 and n<=20:
        print("Weird")
    elif n>=2 and n<=5 or n>20:
        print("Not Weird")

#operações Aritméticas
def operacoesAritmeticas(a, b):
	print(a+b,"\n",a-b,"\n",a*b)
    #print(a-b)
    #print(a*b)

#divisão
def divisoes(a, b):
	print(a//b, "\n", a/b)

if __name__ == '__main__':
	Hello()
	operacoesAritmeticas(10, 4)
	if_else(4)
	divisoes(2, 5)