birthdate= input("Introduce your birthdate in format dd/mm/yyyy: ")
day, month, year = birthdate.split('/')
day = day.zfill(2)
month = month.zfill(2)
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
