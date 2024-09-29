import openpyxl
import os

def main():
    wb = openpyxl.load_workbook('example.xlsx')
    sl = dict()
    for i in wb.sheetnames:
        sl[i] = []
    print(sl)
if __name__ == '__main__':
    main()
