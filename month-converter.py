convert_month = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}

user_input = input("Enter month shortcut: ")
result = convert_month.get(user_input)

if result:
    print(result)
else:
    print("Invalid month!")