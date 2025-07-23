# 🧮 BMI Calculator with GUI, History & Graphs

This is a simple Python project that calculates Body Mass Index (BMI) using a GUI. It allows users to:

- Input weight and height
- See their BMI and category
- Save BMI data per user
- View historical BMI data with graphs 📊

## 💻 Features

- Built with `Tkinter` for GUI
- Simple JSON file storage
- BMI categories based on WHO standards
- Plot BMI trends using `matplotlib`

## 🚀 How to Run

1. Clone this repo or download the ZIP:

```bash
git clone https://github.com/your-username/BMI-Calculator-GUI.git
cd BMI-Calculator-GUI
```

2. Install required library:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python bmi_calculator.py
```

## 📂 Data Storage

All user BMI records are saved in `data/bmi_history.json`. Each record contains:

- Name
- Weight
- Height
- BMI
- Category
- Timestamp

---


