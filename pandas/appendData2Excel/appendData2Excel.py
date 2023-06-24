import pandas as pd
import os
import sys

file1,tab1 = sys.argv[1]+".xlsx", sys.argv[1]
#give filename and sheet name manualy 
#file1,tab1 ="FileName.xlsx","Sheet1"

row_index="job"
col_Values="balance"
outValues="sum"  #sum or count
#if you want to open output file after adding then keep openFile=1 else openFile=0
openFile=1



df=pd.read_excel(open(file1, 'rb'),sheet_name=tab1)
df2=pd.read_excel(open('data.xlsx', 'rb'),sheet_name='data')

if outValues=="count":
    agValue=pd.Series.nunique
else:
    agValue="sum"

#Code

if len(df2.columns.difference(df.columns))<1:
    df2=pd.concat([df2,df],ignore_index=True)
    print("Total lenght: "+str(len(df2)))
    df2 = df2.drop_duplicates()
    print("Total lenght After droping duplicates: "+str(len(df2)))
else:
    print(sys.argv[1]+".xlsx  columns are not matching with data.xlsx workbook")
    sys.exit()


#table = pd.pivot_table(df, values='balance', index=['job'],aggfunc='sum').reset_index()
table = pd.pivot_table(df, values=col_Values, index=row_index,aggfunc=agValue).reset_index().sort_values(by=col_Values, ascending=False)


with pd.ExcelWriter("data.xlsx") as writer:
    df2.to_excel(writer, sheet_name="data",index=0) 
    table.to_excel(writer, sheet_name="table",index=0)


if openFile==1:
    os.system('start excel data.xlsx')   