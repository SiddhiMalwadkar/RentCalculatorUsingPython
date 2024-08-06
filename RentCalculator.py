import tkinter as tk
from tkinter import messagebox

class BillCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bill Calculator")
        self.window.geometry("400x300")  # Set the window size
        self.window.configure(bg="#f0f0f0")  # Set the background color

        # Create a header label
        self.header_label = tk.Label(self.window, text="Bill Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.header_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create input fields
        self.rent_label = tk.Label(self.window, text="Enter your hostel/flat rent:", font=("Arial", 12), bg="#f0f0f0")
        self.rent_label.grid(row=1, column=0, padx=10, pady=5)
        self.rent_entry = tk.Entry(self.window, font=("Arial", 12), width=20)
        self.rent_entry.grid(row=1, column=1, padx=10, pady=5)

        self.food_label = tk.Label(self.window, text="Enter the amount of food ordered:", font=("Arial", 12), bg="#f0f0f0")
        self.food_label.grid(row=2, column=0, padx=10, pady=5)
        self.food_entry = tk.Entry(self.window, font=("Arial", 12), width=20)
        self.food_entry.grid(row=2, column=1, padx=10, pady=5)

        self.electricity_spend_label = tk.Label(self.window, text="Enter the total of electricity spend:", font=("Arial", 12), bg="#f0f0f0")
        self.electricity_spend_label.grid(row=3, column=0, padx=10, pady=5)
        self.electricity_spend_entry = tk.Entry(self.window, font=("Arial", 12), width=20)
        self.electricity_spend_entry.grid(row=3, column=1, padx=10, pady=5)

        self.charge_per_unit_label = tk.Label(self.window, text="Enter the charge per unit:", font=("Arial", 12), bg="#f0f0f0")
        self.charge_per_unit_label.grid(row=4, column=0, padx=10, pady=5)
        self.charge_per_unit_entry = tk.Entry(self.window, font=("Arial", 12), width=20)
        self.charge_per_unit_entry.grid(row=4, column=1, padx=10, pady=5)

        self.persons_label = tk.Label(self.window, text="Enter the number of persons living in room/flat:", font=("Arial", 12), bg="#f0f0f0")
        self.persons_label.grid(row=5, column=0, padx=10, pady=5)
        self.persons_entry = tk.Entry(self.window, font=("Arial", 12), width=20)
        self.persons_entry.grid(row=5, column=1, padx=10, pady=5)

        # Create calculate button
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_bill, font=("Arial", 12, "bold"), bg="#4CAF50", fg="#ffffff")
        self.calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Create output label
        self.output_label = tk.Label(self.window, text="", font=("Arial", 12), bg="#f0f0f0")
        self.output_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def calculate_bill(self):
        try:
            rent = int(self.rent_entry.get())
            food = int(self.food_entry.get())
            electricity_spend = int(self.electricity_spend_entry.get())
            charge_per_unit = int(self.charge_per_unit_entry.get())
            persons = int(self.persons_entry.get())

            total_bill = electricity_spend * charge_per_unit
            output = (food + rent + total_bill) // persons

            self.output_label.config(text=f"Each person will pay: {output}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = BillCalculator()
    calculator.run()
