from datetime import date
def age():
    print("Enter your year of birth")
    yob=int(input())
    today=date.today().year
    age=today-yob
    if age<18:
        print("Minor")
    elif(age>=18 and age<=36):
        print("Youth")
    else:
        print("You are an elder")
age()

