ONE_HOUR_IN_SECONDS = 3600
ONE_MINUTE_IN_SECONDS = 60


def watch(hour, minute):
    ask_hour = int(input("Enter time "))
    ask_minutes = int(input("Enter minutes "))

    result_hour = ask_hour * hour 
    result_minutes = ask_minutes * minute

    print("In " + str(ask_hour) + " hour and " + str(ask_minutes) + " minutes there is " + str(result_hour + result_minutes) + " seconds")


if __name__ == "__main__":
    watch(ONE_HOUR_IN_SECONDS, ONE_MINUTE_IN_SECONDS)