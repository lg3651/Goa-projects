"""3) შექმენით პროგრამა სადაც მომხმარებელი შემოიტანს 5 რციხვს, ხოლო ამ 5 რიცხვს 
შორის გამოიყენეთ ყველა არითმეტიკული ოპერაცია (+,-,*,/,%,//), საბოლოოდ დაბეჭდეთ 
შედეგები ტერმინალში + ახსენით თითოეული ნაწილი კოდის რატომ დაწერეთ კონკრეტული ხაზი და რას აკეთებს."""

num1 = int(input("enter first number: ")) #input lets the user write the value
num2 = int(input("enter second number: "))#int function converts the value type to int
num3 = int(input("enter third number: "))
num4 = int(input("enter fourth number: "))
num5 = int(input("enter fifth number: "))

print (num1 + num2)#plus operator adds up the integers
print (num3 - num4)#minus operator subtracts the integers
print (num4 * num5)#multiplies the integers
print (num3 / num1)#division 
print (num4 % num2)#remainder of num4 divided by num2
print (num2 // num5)#division rounded down to int