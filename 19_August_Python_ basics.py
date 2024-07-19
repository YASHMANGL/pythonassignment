#PYTHON BASIC VARIABLE

#1.Write a program to swap two integer value without assigning  any other variable
a= int(input("Enter 1st number = "))
b= int(input("Enter 2nd number ="))
a,b=b,a            
print("1st number :-",a,"\n2nd number =",b)

#2. Program for calculate the area of rectangle
a=float(input("Enter length of rectangle = "))
b=float(input("Enter width of rectangle = "))
c=a*b
print("Area of rectangle = ",c)

#3.Program for converting Celsius to  Fahrenheit
Celsius_temp=float(input("Enter temperature in Celsius = "))
Fahrenheit_Temp=1.8*Celsius_temp+32
print("Temperature in Fahrenheit = ",Fahrenheit_Temp)


#STRING BASED QUESTION
#1.Taking input as a string and find its total length
a=input("Enter string ")
print("Length of given string = ",len(a))

#2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.
string=input("Enter sentence : ")
lower_string=string.lower()

count=0
vowel="aeiou"
for i in lower_string:
    if i in vowel:
        count+=1
print(count)

# 3. Given a string, reverse the order of characters using string slicing and print the reversed string.
string = input("Enter a string : ")
reversed_string= string[::-1]
print(reversed_string)

# 4. Write a program that takes a string as input and checks if it is a palindrome
string=input("Enter string : ")
reversed_string = string[::-1]

if (string==reversed_string):
    print("Given string is palindrome.")
else:
    print("Given string is not palindrome .")

# 5. Create a program that takes a string as input and removes all the spaces from it. Print the modified string without spaces.
string=input("Enter string : ")
modified_string=string.replace(" ","")
print(modified_string)