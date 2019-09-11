from banner import banner

banner("BIRTHDAY", "Mr. Baldus")

# 1. Find out when you were born
# 2. Figure out how many days until your birthday
# 3. Print information about the birthday: Days until, Days ago, or Happy B-Day

def main():
    get_birthday_info()
    compute_days_between_dates()
    print_birthday_info()

def get_birthday_info():
    print("When were you born?")
    year = input("Year [YYYY]: ")
    month = input("Month [MM]: ")
    day = input("Day [DD]: ")

def compute_days_between_dates():
    pass

def print_birthday_info():
    pass



main()