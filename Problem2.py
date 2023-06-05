term1 = 1
term2 = 2
previous = term1
temp = term2
Sumofevenumber = 0 
#temp1= 0

while (temp <= 4000000):
    if temp % 2 ==0:
        Sumofevenumber = Sumofevenumber + temp
        temp1 = temp + previous
        previous = temp
        temp = term2
        
print("Sum of even number is :",Sumofevenumber)        
        
    