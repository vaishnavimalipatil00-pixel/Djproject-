import pandas as pd
import glob

def load_attendance():
    files = glob.glob("data/*.xlsx")
    df_list = []

    for file in files:
        data = pd.read_excel(file)
        df_list.append(data)

    return pd.concat(df_list)

def load_students():
    return pd.read_csv("data/students.csv")

def merge_data():
    attendance = load_attendance()
    students = load_students()
    return attendance.merge(students, on="Student_ID")
