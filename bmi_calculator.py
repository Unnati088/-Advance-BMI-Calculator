import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os
import matplotlib.pyplot as plt

DATA_FILE = "data/bmi_history.json"

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def save_bmi_data(name, weight, height, bmi, category):
    if not os.path.exists("data"):
        os.makedirs("data")

    entry = {
        "name": name,
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def plot_history(name):
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except:
        messagebox.showerror("Error", "No history data found.")
        return

    user_data = [d for d in data if d["name"].lower() == name.lower()]
    if not user_data:
        messagebox.showinfo("No Data", f"No BMI history for {name}.")
        return

    dates = [d["date"] for d in user_data]
    bmis = [d["bmi"] for d in user_data]

    plt.figure(figsize=(8, 4))
    plt.plot(dates, bmis, marker="o")
    plt.title(f"BMI History for {name}")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()

def calculate_bmi():
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if not name:
            raise ValueError("Name is required.")
        if not (20 <= weight <= 300):
            raise ValueError("Weight should be between 20kg and 300kg.")
        if not (0.5 <= height <= 2.5):
            raise ValueError("Height should be between 0.5m and 2.5m.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        return

    bmi = round(weight / (height ** 2), 2)
    category = get_bmi_category(bmi)

    result_label.config(text=f"BMI: {bmi} ({category})")
    save_bmi_data(name, weight, height, bmi, category)

def show_graph():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Required", "Please enter your name to view history.")
    else:
        plot_history(name)

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m)").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

tk.Button(root, text="Show BMI History Graph", command=show_graph).pack(pady=10)

root.mainloop()
