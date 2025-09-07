income=int(input("what is your monthly income? $"))
expense=int(input("how much are your total monthly expenses? $"))
savings=income-expense

if expense>=income:
    print("you better control your expenses as your savings are nil\nspend on things which you really need")
elif savings>=income:
    print("youre saving a little too much dude spend some please")
else:
    print("you're good on budget")

print(f"savings= ${savings}")