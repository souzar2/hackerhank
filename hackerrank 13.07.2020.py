
#função que mostra se o ano é bissexto
def is_leap(year):
    leap = False
    
    if year %4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0: 
                leap = True
    return leap 


if __name__ == 'main':
	is_leap(2015)

	n = 3
    t = ''
    	for i in range(n):
       		t += str(i+1)
	print(t)