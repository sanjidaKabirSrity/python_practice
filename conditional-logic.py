print(2==3)
print(3==3)
print(2>3)
print(2<3)
print(2!=3)
print(3!=3)
print(2>=3)
print(2<=3)

print("Bangladesh" == 'Bangladesh')
print("Bangladesh" == 'bangladesh')

# List
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number_list)
print(number_list[0])
print(number_list[5])
#print(number_list[10]) # Error dekhabe


# Length use to len() function
saarc = ['Bangladesh', 'Afghanistan', 'Bhutan', "Nepal", "India", "Pakistan", "Sri Lanka"]
print(saarc)
print(saarc[0])
print("Number of countries in SAARC: ", len(saarc))

print("India" in saarc)
print("China" in saarc)
print("China" not in saarc)

# if, elif, else statement

saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
country = input("Enter the name of the country: ")

if country in saarc:
    print(country, "is a member of SAARC")
else:
    print("The country is not a member of SAARC")
print("Program terminated")

# Grade Number
marks = int(input("Please enter your marks: "))

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
else: 
    grade = "F"

print("Your grade is" , grade)

# Leap Year
year = int(input("Enter a year: "))

if year%4 == 0 :   # system-1
    print("Yes")
else:
    if year%100 == 0 :
        if year%400 == 0 :
            print("Yes")
        else:
            print("no")
    else:
        print("no")

if year%400 == 0 :  # system-2
    print("Yes")
elif year%100 == 0 :
    print("No")
elif year%4 == 0 :
    print("Yes")
else:
    print("No")

if year%100 != 0 and year%4 == 0 :  # system-3
    print("Yes")
elif year%100 == 0 and year%400 == 0 :
    print("Yes")
else:
    print("No")
