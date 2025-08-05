import tkinter as tk

#This function calculates the income tax in terms of the monthly salary and ta period
def calculate_tax():
    try:
        salary = float(salary_entry.get())
        tax_period = tax_period_var.get()
        #This block of code converts the salary to annual if necessary
        if tax_period == "monthly":
            annual_salary = salary * 12
        else:
            annual_salary = salary
          #Income tax brackets  
        if annual_salary <= 237100:
            tax = annual_salary * 0.18
            
        elif 237101 <= annual_salary <= 370500:
            tax = 42678 + (annual_salary - 237100) * 0.26

        elif 370501 <= annual_salary <= 512800:
            tax = 77362 + (annual_salary - 370500) * 0.31

        elif 512801 <= annual_salary <= 673000:
            tax = 121475 + (annual_salary - 512800) * 0.36
            
        elif 673001 <= annual_salary <= 857900:
            tax = 179147 + (annual_salary - 673000) * 0.39  
             
        elif 857901 <= annual_salary <= 1817000:
            tax = 251258 + (annual_salary - 857900) * 0.41  
            
        else:
            tax = 644489 + (annual_salary - 1817000) * 0.45
            
        #This blockk of code converts back to monthly tax when necessary    
        if tax_period == "monthly":
            tax = tax / 12
        
       
        tax_label.config(text ="Income tax: {:.2f}".format(tax))
        
    except ValueError:
        tax_label.config(text = "Please enter the correct salary!") #This error message will be displayed if the user enters an invalid input
  
def validate_tax_period(value): #This function validates the ta period input
    if value() in ["Monthly", "Yearly"]:
        return True
    else:
        return False
              
root = tk.Tk()
root.title("Income tax calculator")

#Creates the input form
salary_label = tk.Label(root, text= "Please enter your monthly salary:")
salary_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
salary_entry = tk.Entry(root)
salary_entry.grid(row=0, column=1, padx=10, pady=5)

tax_period_label = tk.Label(root, text="Yearly/Monthly:")
tax_period_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
tax_period_var = tk.StringVar(value="Monthly")
tax_period_entry = tk.Entry(root, textvariable=tax_period_var, validate="key", validatecommand=(root.register(validate_tax_period), '%P'))
tax_period_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate income tax", command=calculate_tax)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

tax_label = tk.Label(root, text="Income tax:")
tax_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
tax_result_label = tk.Label(root, text="")
tax_result_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")

root.mainloop()            
            
            
            
            
            
            
            
            
            
            
            
            