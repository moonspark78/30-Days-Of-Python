#Day 2: 30 Days of python programming

#level 1
first_name = "John";
last_name= "Elton";
full_name= first_name + " " + last_name;
country= "US";
city= "San Francisco";
age=20;
year = 2009;
is_married = True;
is_true = True;
is_light_on = True;
email, user = "John@gmail.com", "johnelton";


#Exercises: Level 2
# 1-
print(type(first_name));
print(type(last_name));
print(type(full_name));
print(type(country));
print(type(city));
print(type(age));
print(type(year));
print(type(is_married));
print(type(is_true));
print(type(is_light_on));
print(type(email));
print(type(user));


# 2-
print(len(first_name));

# 3-
print(len(first_name) > len(last_name));

# 4-
num_one= 5; 
num_two= 4;
total = num_one + num_two;
diff = num_one - num_two;
product= num_one*num_two;
division = num_one/num_two;
remainder= num_two%num_one; 
exp = num_one**num_two;
floor_division= num_one // num_two;

# 5-
import math
area_of_circle= math.pi * 30**2

circum_of_circle= math.pi * (30*2)

radius = int(input("quelle est le rayon"))
area = math.pi * radius**2

# 6-
first = input("Enter your first name:")
last = input("Enter your last name:")
country = input("Enter your country:")
age = int(input("Enter your age:"));

# 7-
help('keywords')