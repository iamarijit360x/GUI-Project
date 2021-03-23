import os
import openpyxl
import pathlib
global loc
loc=os.path.dirname(__file__) +'\studentlogininfo.xlsx'
def check_email_present(email):
    check_file(loc)
    book =openpyxl.load_workbook(loc)
    sheet = book.active
    for i in range(1,sheet.max_row+1):
        if(((sheet.cell(row=i,column=1)).value)==email):
            return True
    return False

def check_file(loc):
    file = pathlib.Path(loc)
    if not(file.exists()):
        data=["Email","Password"]
        wb =openpyxl.workbook.Workbook()
        ws0 = wb.worksheets[0]
        ws0.append(data)
        wb.save(filename =loc)
def save_xls_file(arr,loc):
    workbook_name =loc
    wb =openpyxl.load_workbook(workbook_name)
    page = wb.active
    page.append(arr)
    wb.save(filename =workbook_name)

#arr=['arijit.bandyos7@gmail.com','1234']

