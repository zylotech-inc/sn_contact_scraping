from logging import exception
import time
from black import out
import pandas as pd
import sqlite3
import os
from pathlib import Path

cd = os.path.abspath(__file__)
fileDirectory = os.path.dirname(cd)
parentDirectory = os.path.dirname(fileDirectory)
currenttime = str(time.asctime()).replace(":","_").replace(" ","_")

input_file_path = Path(parentDirectory +'\snscraping\input\input.xlsx')

def readinginput():
    """ Reads excel file in pandas df which has Code, Company, Country & Filter Column.

    Param:
        None
    Returns:
        list: [company,filter,code]
    """
    try:
        data = pd.read_excel(input_file_path)       
    except:
        raise exception ("Please Check input file")

    try:
        code = data['Code'].to_list()
        company = data['Companies'].to_list()
        filter = data['Filter'].to_list()
    except:
        raise Exception ('Please Check file columns (Code,Companies,Filter)')

    print("Input file read Successfully")
    return [company,filter,code]
    


def reading_cred():
    """Reading Excel file in pandas df for linkedin Cred.

    Param:
        None
    Raises:
        Exception: Please Check Excel File
        Exception: Please Check ID & Password
    Returns:
        list: [str, str]
    """

    try:
        data = pd.read_excel(input_file_path,sheet_name="Login")
    except:
        raise Exception('Please Check Excel file and Sheet "Login"') 

    try:
        id = data['ID'].to_list()[0]
        password = data['Password'].to_list()[0]
        if len(id) <3  or len(password) <3:
            raise Exception ('Please Check "ID & Password" in the excel sheet')

    except:
        raise Exception ('Please Check "ID & Password" in the excel sheet')
    
    return [id,password]


def output_db():
    """Creates Sqlite db and table (Code, Input_Company, Contact_Name, Title, Output_Company, Location, Profile_url, More_Employees, Output_company_Url) to store scraped result.
    
    Param:
        None
    Returns:
        object: db connetion
    """
    con = sqlite3.connect(Path(parentDirectory + '\snscraping\database\\' + currenttime + '_output.db'))
    cur = con.cursor()
    cur.execute("create table if not exists contacts(Code,Input_Company,Contact_Name,Title,Output_Company,Location,Profile_url,More_Employees,Output_company_Url)")   
    return con


def saveoutput(outputlist):
    """ Saves scraped result in sqlite db

    Param:
        outputlist (list): list[Code, Input_Company, Contact_Name, Title, Output_Company, Location, Profile_url, More_Employees, Output_company_Url]
    """
    con = output_db()
    cur = con.cursor()
    cur.execute("insert into contacts values(?,?,?,?,?,?,?,?,?)",outputlist)
    con.commit()