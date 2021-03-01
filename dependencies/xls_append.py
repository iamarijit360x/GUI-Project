from openpyxl import load_workbook
from openpyxl.workbook import Workbook
import xlsxwriter
import pathlib

def check_file(loc):
    
    '''Checks if the file is present or not'''
    
    file = pathlib.Path(loc)
    
    if not(file.exists()):
        
        data=["Registration Number","Name",'DOB',"Father's Name","Mother's Name","Gender",'Dept','Domicile','Mother\'s Phone Number','Father\'s Phone Number','Email Id'] #first row
        wb = Workbook()
        page = wb.active
        page.append(data)
        wb.save(filename =loc)
        
def save_xls_file(arr,loc):
    
    '''saves the arr attributes into the excel file'''
    
    workbook_name =loc
    wb =load_workbook(workbook_name)
    page = wb.active
    sheet = wb.worksheets[0]
    reg='ST169/'+str(sheet.max_row)
    arr.insert(0,reg)
    page.append(arr)
    wb.save(filename =workbook_name)
    
if __name__ == '__main__':
    
    loc=os.path.dirname(__file__) +'\studentinfo.xlsx'
    check_file(loc)