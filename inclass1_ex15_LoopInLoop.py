numDays = 7
numWeeks = 4

for week in range(1, numWeeks + 1):
    # end="" avoids pointer going to new line.
    print("week " + str(week) + ": ", end="")

    # Show days of week
    for day in range(1, numDays + 1):
        if day == 1:
            dayName = "Sunday1";
        elif day == 2:
            dayName = "Monday2"
        elif day == 3:
            dayName = "Tuesday3"
        elif day == 4:
            dayName = "Wednesday4"
        elif day == 5:
            dayName = "Thursday5"
        elif day == 6:
            dayName = "Friday6"
        elif day == 7:
            dayName = "Saturday7"
        print(dayName + "   ", end="");

    print("")  # Goes to new line
