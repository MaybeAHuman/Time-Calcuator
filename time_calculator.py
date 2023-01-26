# Create cycle function that will take list and integer returns number of time it has done full cycle and last item it has stopped at
# integer for number of times you want cycle through and list item of which you want cycle through
def cycle(cycle_list, n_cycle):
    n_full_cycle = n_cycle // len(cycle_list)
    n_part_cycle = n_cycle % len(cycle_list)
    last_item = cycle_list[n_part_cycle]

    return n_full_cycle, last_item

def add_zero(t):
    if t < 10:
        return f"0{t}"
    else:
        return str(t)


def add_time(start, duration, weekday=None):
    # Split start and duration time into list
    start_list = start.replace(":", " ").split(" ")
    duration_list = duration.replace(":", " ").split(" ")

    # Create list of hours and minutes
    hours_list = [i for i in range(1, 13)]
    minutes_list = [i for i in range(0, 60)]

    # Create current hour and minute variable
    current_hour_index = hours_list.index(int(start_list[0]))
    current_minute_index = minutes_list.index(int(start_list[1]))

    # Create variable of hours and minutes that have to add
    add_hour = int(duration_list[0])
    add_minute = int(duration_list[1])

    # Create list AM/PM
    merdiem_list = ["AM", "PM"]

    # Save index value of current meridiem
    meridiem_index = merdiem_list.index(start_list[2]) #AM -> Ante Meridiem, PM -> Post Meridiem

    # Now first cycle through minutes and hour
    extra_hour, new_minute = cycle(minutes_list, current_minute_index + add_minute)
    extra_merdiem, new_hour = cycle(hours_list, current_hour_index + add_hour + extra_hour)
    
    t = (current_hour_index + add_hour + extra_hour) % 12

    if t == 11:
        extra_merdiem += 1

    extra_day, new_mediem = cycle(merdiem_list, extra_merdiem + meridiem_index)
    new_minute = add_zero(new_minute)

    # Create list of weekdays
    weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Save index value of current weekday into variable if current weekday is not None
    if weekday != None:
        weekday_index = weekday_list.index(weekday.capitalize())
        extra_week, new_weekday = cycle(weekday_list, weekday_index + extra_day)
    
        if extra_day == 0:
            return f"{new_hour}:{new_minute} {new_mediem}, {new_weekday}"
        elif extra_day == 1:
            return f"{new_hour}:{new_minute} {new_mediem}, {new_weekday} (next day)"
        elif extra_day > 1:
            return f"{new_hour}:{new_minute} {new_mediem}, {new_weekday} ({extra_day} days later)"
    else:
        if extra_day == 0:
            return f"{new_hour}:{new_minute} {new_mediem}"
        elif extra_day == 1:
            return f"{new_hour}:{new_minute} {new_mediem} (next day)"
        elif extra_day > 1:
            return f"{new_hour}:{new_minute} {new_mediem} ({extra_day} days later)"


print(add_time("11:59 PM", "24:05", "wednesday"))