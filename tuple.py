tuple = "monday,tuesday,wednesday,thursday,friday,saturday"
day_num = int(input("Enter the day number(1-7): "))
day = tuple[day_num - 1]
print(f"the day {day_num} is {day}")