history = []
while True:

    try:
        a = int(input("Enter a first number: "))
        b = int(input("Enter a second number: ")) 

        print(f"what kind of Operations do you want to perform\nPress + for Addition\nPress - for Subtraction\nPress * for Multiplication\nPress / for Division")
    
        o =input("Enter operations") 
        if o == "h":
            if not history:
                print("No history yet")
            else:
                for item in history:
                    print(item)  
            continue      

        match o:
            case "+":
                print(f"The result is: {a + b}")
                history.append(f"{a} + {b} = {a + b}")
            case "-":
                print(f"The number is: {a - b}") 
                history.append(f"{a} - {b} = {a - b}")        

            case "*":
                print(f"The number is: {a * b}")
                history.append(f"{a} * {b} = {a * b}")

            case "/":
                if b==0:
                    print("Cannot divide by zero")   
                else:
                    print(f"The number is: {a / b}")
                    history.append(f"{a} / {b} = {a / b}")
    
        
            case default:
                print("There was an error")



    except Exception as e:
        print(e) 

    choice = input("Do you want to continue y/n :")  
    if choice =="n":
        break



