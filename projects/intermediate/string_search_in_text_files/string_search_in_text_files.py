# This program searches a Directory and Sub Directories 
# for a piece of text located inside a file

import os
import fnmatch
import argparse

search_dir = "/github/python-projects/dirwithtxtfiles"
search_files = "*.txt"

def searchText(search_string):
    for path,dirs,files in os.walk(search_dir):
        for file in files:
            if fnmatch.fnmatch(file, search_files):
                fullname = os.path.join(path,file)
                openedfile = open(fullname)                                                                             
                for line in openedfile:
                    if search_string in line:
                        print(line)
                        print(openedfile) 

if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description='This program searches a Directory and Sub Directories for a given string')
    parser.add_argument('-s','--searchstr', help='Enter a string which you want to search in files', required=True)
    args = parser.parse_args()
    searchText(args.searchstr)
