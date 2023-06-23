import pandas as pd
import sys
import os

#input fields
print("input file:"+sys.argv[1])
#if filename and sheet name are same
file1,tab1 = sys.argv[1]+".xlsx", sys.argv[1]
#give filename and sheet name manualy 
#file1,tab1 ="FileName.xlsx","Sheet1"

row_index="Cabin"
col_Values="PassengerId"
outValues="count"  #sum or count
#if you want to open output file after adding then keep openFile=1 else openFile=0
openFile=1



#Code
df=pd.read_excel(open(file1, 'rb'),sheet_name=tab1)
print("File1 count:",df.shape[0])

if outValues=="count":
    agValue=pd.Series.nunique
else:
    agValue="sum"

table = pd.pivot_table(df, values=col_Values, index=row_index,aggfunc=agValue).reset_index().sort_values(by=col_Values, ascending=False)
outFile="Res_"+file1
print("Generated File: ",outFile)
with pd.ExcelWriter(outFile) as writer:
    table.to_excel(writer, sheet_name="table",index=False)
    df.to_excel(writer, sheet_name=tab1,index=False)
    

if openFile==1:
    os.system('start excel "'+outFile+'"')


