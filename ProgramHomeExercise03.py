# Exercise 1 + bonus question
id_num: str = input("Please enter your id number: ");
f_name: str = input("Please enter your first name: ");
l_name: str = input("Please enter your last name: ");
height: float = float(input("Please enter your height: "));
b_date_year: int = int(input("Please enter the year of your birth date: "));

id_num1: str = input("Please enter your id number: ");
f_name1: str = input("Please enter your first name: ");
l_name1: str = input("Please enter your last name: ");
height1: float = float(input("Please enter your height: "));
b_date_year1: int = int(input("Please enter the year of your birth date: "));

id_num2: str = input("Please enter your id number: ");
f_name2: str = input("Please enter your first name: ");
l_name2: str = input("Please enter your last name: ");
height2: float = float(input("Please enter your height: "));
b_date_year2: int = int(input("Please enter the year of your birth date: "));

print(f"#id: {id_num:<10} name: {l_name + ',' + f_name:<20} height: {height:.2f} year-of-birth: {b_date_year:}");
print(f"#id: {id_num1:<10} name: {l_name1 + ',' + f_name1:<20} height: {height1:.2f} year-of-birth: {b_date_year1}");
print(f"#id: {id_num2:<10} name: {l_name2 + ',' + f_name2:<20} height: {height2:.2f} year-of-birth: {b_date_year2}");

# Exercise 2
grade: int = int(input("Please enter your grade: "));
if 96 <= grade <= 100:
    print("excellent!!! You're Star!");
elif 81 <= grade < 96:
    print("awesome!");
elif 61 <= grade < 81:
    print("pretty good");
elif 41 <= grade < 61:
    print("you're getting there, need some more work");
elif 0 <= grade < 41:
    print("try harder next time...");
else:
    print("illegal grade");

# Exercise 3
vol: int = int(input("Please enter the volume level: "));
match vol:
    case 0:
        print("mute");
    case 1:
        print("very quiet");
    case 2:
        print("very quiet");
    case 3:
        print("quiet");
    case 4:
        print("moderately quiet");
    case 5:
        print("medium");
    case 6:
        print("moderately loud");
    case 7:
        print("loud");
    case 8:
        print("very loud");
    case 9:
        print("extremely loud");
    case 10:
        print("extremely loud");
    case _:
        print("Invalid volume level.");

# Exercise 4
num: int = int(input("Please enter a number: "));
if num % 7 == 0:
    print("seven boom");
else:
    print("not seven boom");

# Exercise 5
num: int = int(input("Please enter a number: "));
if num % 5 == 0 and num % 3 == 0:
    print("Fizz Buzz");
elif num % 3 == 0:
    print("Buzz");
elif num % 5 == 0:
    print("Fizz");
else:
    print("not divisible by 3 or 5 or both");

# bonus question
# Exercise 1
pizza_num: int = int(input("Please enter a number of pizza slices: "));
if pizza_num % 4 == 0:
    print(f"Each friend received {pizza_num // 4} slices of pizza, and no more slices remained.");
else:
    print(f"Each friend received {pizza_num // 4} slices of pizza, and {pizza_num % 4} more slices remained.");

# Exercise 2
pizza_num: int = int(input("Please enter a number of pizza slices: "));
friends_num: int = int(input("Please enter a number of friends: "));
if pizza_num % friends_num == 0:
    print(f"Each friend received {pizza_num // friends_num} slices of pizza, and no more slices remained.");
else:
    slices_remain: int = pizza_num % friends_num;
    print(f"Each friend received {pizza_num // friends_num} slices of pizza, and {slices_remain} more slices remained.");
