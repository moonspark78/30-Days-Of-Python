#Operators

#1
age = 23;

#2
height=float(178);

#3
complix = 2 +4j;
c_number = complex(3,4);

#4
base = int(input("Entrer base : "))
height = int(input("Entrer height : "))
area =  int(0.5 * base * height);
print("The area of the triangle is  ", area)


#5
side_a = int(input("Enter side a : "));
side_b = int(input("Enter side b : "));
side_c = int(input("Enter side c : "));
perim = (side_a+side_b+side_c)
print("The perimeter of the triangle is" , perim); 


#6
length = int(input("Enter length : "));
width = int(input("Enter width : "));
area = length * width;
perimeter = 2 * (length + width)
print("The area and the perimeter of the rectangle is ", area, perimeter);


#7
radius = int(input("Enter radius : "));
area = 3.14 * radius * radius;
circumference=  2 * 3.14 * radius;
print("the area and the circumference of the circle is : ", area, "," ,circumference);


#8
print("x-intercept", 1)
print("y-intercept", -2)
print("slope", 2)

#9
import math
x1, x2, y1, y2 = 2, 6, 2, 10;
slope = ((y2 - y1)/(x2-x1))
print("Slope : ", slope)
distance = math.sqrt((x1 - x2)**2+ (y1 - y2)**2);
print("Distance : ", distance);


#10
#resultat_si_vrai if (condition) else (resultat_si_faux)
x1, x2, y1, y2 = 2, 6, 2, 10;
print(2 if 2 < (y2 - y1)/(x2-x1) else (y2 - y1)/(x2-x1))


#11
for x in range(0,9):
    print(x **2 +6 * x + 9)

#12
print(len("python"))
print(len("dragon"))
print(len("python") > len("dragon"))
print(not(len("python") == len("dragon")))

#13
print("on" in "dragon" and "on" in "python" )

#14
print("jargon" in "I hope this course is not full of jargon.")

#15
print(not("on" in "dragon" and  "on" in  "python"))

#16
#print(len("python"))
print(str(float(len('python'))))

#17
number = int(input("entrer un nombre : "))
print("Even" if number % 2 == 0 else "Odd")

#18
print(7//3 == int(2.7))

#19
print(type("10") == type(10))
#20
print(int('9.8') == 10)
print(int('9.8') == 10)

#21
hours=int(input("Enter hours: : "))
rph=int(input("rate per hour: "))
print("Earing", hours*rph)

#22
#un an il y a 60 x  60 x  24 x  365
years=int(input("Enter number of years you have lived : "));
print("You have lived for", years * 60 *  60 *  24 *  365 ,"seconds")

#23
for i in range(1,6):
    print(i, i**0, i**1, i**3, i**3)
