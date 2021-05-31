while True:
    try:
        user_input = input("Cuál es el total de su cheque? > $")
        total_check = float(user_input)
        break 
    except ValueError:
        print("Lo siento, parece que escribiste algo incorrectamente. Intente escribir un número! :)")

# In this next loop, there is no try hermmmm 
# that was my Yoda impression
# Here it will loop unless you type in exactly what is in the () 
while True:
    tip_choice = input("Escriba 'a' para 15%, 'b' para 18%, o 'c' para 20% > ")
    if tip_choice not in ('a', 'b', 'c'):
        print("Lo siento, parece que escribiste algo incorrectamente. Lea las instrucciones y vuelva a intentarlo.!")
    else:
        if tip_choice == "a":
            result = .15 * total_check  
        elif tip_choice == "b":
            result = .18 * total_check
        elif tip_choice == "c":
            result = .20 * total_check
        
        print("You should leave $%.2f " % (result))
        break