import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

df = pd.DataFrame()

def help():
    print("""
          help: returns list of commands and function
          setfile: sets the csv file to use for various functions
          print: prints out the csv file being used in the program
          export: exports output data to a csv file
          """)

def setfile():
    desiredfile = input("enter the path of your csv file path:")
    file = pd.read_csv(desiredfile)
    df['Assignment'] = file['Assignment']
    df['Points'] = file['Points']
    chars_to_remove = ['=', '"', " "] 
    df['Points'] = df['Points'].str.translate({ord(char): None for char in chars_to_remove})
    df['Points'] = df['Points'].str.split('/')
    
def printfile():
    print(df)

def onetoone():
    print('test')

def export():
    df.to_csv('export.csv')

def home():
    var = input()
    if var == '!setfile':
        setfile()
        home()
    elif var == '!print':
        printfile()
        home()
    elif var == '!help':
        help()
        home()
    elif var == '!x/x':
        onetoone()
        home()
    elif var == '!export':
        export()
        home()
    else:
        print("Invalid Command")
        home()

print("Welcome, For a list of commands run !help ")
home()
