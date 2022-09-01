#imports 
import pandas as pd
from pandas_profiling import ProfileReport
import tkinter as tk
from tkinter import filedialog

# display 
root = tk.Tk()
root.withdraw()

# get file path
file_path = filedialog.askopenfilename()

# import data in a pandas dataframe
df = pd.read_excel(file_path)

# use the filepath to generate pandas profiling
profile = ProfileReport(df, title="Pandas Profiling Report")

profile.to_file("your_report.html")