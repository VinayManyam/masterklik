import pandas as pd
import os

#input fields
file1,tab1 = "test.xlsx", "test"
file2,tab2 = "train.xlsx", "train"
outputFile="Res.xlsx"
#if you want to open output file after adding then keep openFile=1 else openFile=0
openFile=1


#Code
df=pd.read_excel(open(file1, 'rb'),sheet_name=tab1)
print("File1 count:",df.shape[0])
df1=pd.read_excel(open(file2, 'rb'),sheet_name=tab2)
print("File2 count:",df1.shape[0])

df_new=pd.DataFrame()
df_new=pd.concat([df, df1],ignore_index=True)
print("Total:",df_new.shape[0])
df_new = df_new.drop_duplicates()
print("Total After deleting duplicates:",df_new.shape[0])

with pd.ExcelWriter(outputFile) as writer:
    df_new.to_excel(writer, sheet_name="Total",index=False) 
    
print("FileName: ",outputFile)
    
if openFile==1:
    os.system("start " + outputFile)
    





