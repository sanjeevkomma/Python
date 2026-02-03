# Python 3.10+
def day_name(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case _:
            return "Invalid day"


# print(day_name(1)) # Monday
# print(day_name(5)) # Invalid day


#Older Python : Dictionary switch
week_days = {
    1: "Saturday",
    2: "Sunday",
    3: "Thursday",
    4: "Friday" }

print(week_days.get(1, "Invalid day")) # Saturday
print(week_days.get(5, "Invalid day")) # Invalid day











