#3) 1-დან 100-მდე დაითვალეთ ხუთის ჯერადი რიცხვების ჯამი გამოიყენეთ if, else გამოგადგებათ % ნიშანი

sum= 0
for num in range (1,100):
    if num % 5==0:
        sum = sum+num
print (sum)