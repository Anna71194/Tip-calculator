
#import pandas as variable pd
import pandas as pd

#assign varaiable grades as panda.readfunctionfor_csv (The file i want pandas to read)
grades = pd.read_csv("grades.csv")

#grades variable using the . to_excel function to change csv to excel arguments (New file name, sheet name in excel and if we want indexing)
grades.to_excel("Grades.xlsx", sheet_name="Student_Grades", index=False)