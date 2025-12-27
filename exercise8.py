import tkinter as tk
from tkinter import messagebox


def Calculate_share():
    try:
        total_bil = float(ent_TotalBill.get())
        num_people = int(ent_NumberOfPeople.get())

        if total_bil <= 0:
            messagebox.showerror("Error","the price has a grater than 0!")
            return
        
        if num_people <= 0:
            messagebox.showerror("Error","the num of people grater than 0!")
            return
        
        share=total_bil/num_people

        result_label.config(text=f"the price for one people: {share:.2f}")
    except ValueError:
        messagebox.showerror("Error","please enter a number!")
    except ZeroDivisionError:
        messagebox.showerror("Error","the num of people grater than 0!")
    except Exception as e:
        messagebox.showerror("Error",f"the undefind error: {e}")




#GUI
root=tk.Tk()
root.title("Dong-Calculate")
root.geometry("500x300")

input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, pady=20)


label_TotalBill=tk.Label(input_frame,text="enter TotalBill: ",font=("Arial", 12, "bold"))
label_TotalBill.grid(row=0 , padx=40 , pady=10 , column=0 )

ent_TotalBill = tk.Entry(input_frame)
ent_TotalBill.grid(row=0 , padx=10 , pady=10 , column=1 ) 



label_NumberOfPeople=tk.Label(input_frame,text="enter Num of people: ",font=("Arial", 12, "bold"))
label_NumberOfPeople.grid(row=1 , padx=40 , pady=10 , column=0 )

ent_NumberOfPeople = tk.Entry(input_frame)
ent_NumberOfPeople.grid(row=1 , padx=10 , pady=10 , column=1 )


btn_Calculate = tk.Button(root,text="Calculate",bg="#E8E8E8",fg="black",font=("Arial", 12, "bold") ,command=Calculate_share)
btn_Calculate.grid(row=1 , column=0 , columnspan=2 , pady=17 )



result_label = tk.Label(root, text="")
result_label.grid(row=2 , column=0 , pady=20)

root.mainloop()