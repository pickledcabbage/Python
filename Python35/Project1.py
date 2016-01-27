# Project 1: Dmitriy Gutnik 77099786 and Ulises Perez 18374947
from pathlib import Path
from pathlib import PurePath
import os
import shutil

def main():
    #First line of input
    directory_path = input()
    p = None
    while(os.path.exists(directory_path)==False):
        print('ERROR')
        directory_path = input()
    p = Path(directory_path)
    
    #Second line of input
    code = input()
    codelist = str.split(code)
    while (codelist[0] in 'NES')==False:
        print('ERROR')
        code = input()
        codelist = str.split(code)
    file_list = []
    if codelist[0] == 'N':
        temp1 = find_file(p,codelist[1])
        if (temp1 != ''):
            file_list.append(temp1)
        else:
            print("FILE " + codelist[1] + " NOT FOUND!")
    elif codelist[0] == 'E':
        file_list = return_by_ext(p,'.'+codelist[1].replace('.',''))
    else:
        file_list = return_by_size(p,int(codelist[1]))

    #Third line of input
    code2 = input()
    codelist2 = str.split(code2)
    while (codelist2[0] in 'PFDT')==False:
        print('ERROR')
        code2 = input()
        codelist2 = str.split(code2)
    if codelist2[0] == 'P':
        print_interest(file_list)
    elif codelist2[0] == 'F':
        first_line_interest(file_list)
    elif codelist2[0] == 'D':
        duplicate_interest(file_list)
    else:
        touch_interest(file_list)
        

def find_file(p:Path,name:str)->str:
    '''Recursive search function for file name'''
    for f in p.iterdir():
        try:
            if f.is_dir()==False:
                if (f.as_posix() == p.as_posix()+'/'+name):
                    return p.as_posix()+'/'+name
            else:
                temp = find_file(f,name)
                if (temp !=''):
                    return temp
        except PermissionError:
            print('Permission not granted on a file.')
    return ''

def return_by_size(p:Path,size:int)->list:
    '''Recursive search function for file size'''
    templist = []
    for f in p.iterdir():
        try:
            if f.is_dir()==False:
                if (os.stat(f.as_posix()).st_size>=size):
                    templist.append(f.as_posix())
            else:
                templist.extend(return_by_size(f,size))
        except PermissionError:
            print('Permission not granted on a file.')
    return templist

def return_by_ext(p:Path,ext:str)->list:
    '''Recursive search function for extensions'''
    templist = []
    for f in p.iterdir():
        try:
            if f.is_dir()==False:
                if (f.suffix == ext):
                    templist.append(f.as_posix())
            else:
                templist.extend(return_by_ext(f,ext))
        except PermissionError:
            print('Permission not granted on a file.')
    return templist

def print_interest(filelist: list)->None:
    '''For P input in the third line, prints all the file paths'''
    for filepath in filelist:
        print(filepath)

def first_line_interest(filelist: list)->None:
    '''For F input in the third line, prints file paths and their first line'''
    for file in filelist:
        print(file)
        infile = open(file, 'r')
        print(infile.readline().replace('\n',''))
        infile.close()

def duplicate_interest(filelist: list)->None:
    '''For D input in the third line, prints file paths and copies them'''
    for file in filelist:
        print(file)
        shutil.copyfile(file, file + '.dup')

def touch_interest(filelist: list)->None:
    '''For T input in the third line, prints file paths and "touches" files'''
    for file in filelist:
        print(file)
        infile = open(file, 'w')
        infile.close()

if __name__ == '__main__':
    main()
