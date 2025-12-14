import os
import shutil


#Usecase1: I wanted to clean the tmp folder in a predefined path C:\\dataset1\\tmp, if it exists

"""def folder_cleanup():
    actual_path="C:\\Users\\HP\\PycharmProjects\\WE47Usecases\\dataset1"
    try:
            shutil.rmtree(actual_path)
            print("Folder remove successfully from the path", actual_path)
    except FileNotFoundError as e:
            print("Folder remove failed due to", e)

folder_cleanup()"""
#or

def folder_cleanup2():
    actual_path="C:\\Users\\HP\\PycharmProjects\\WE47Usecases\\dataset1"
    try:
         if os.path.exists(actual_path):
            shutil.rmtree(actual_path)
            print("Folder remove successfully from the path", actual_path)
         else:
             raise FileNotFoundError
    except FileNotFoundError as e:
            print("Folder remove failed due to folder doesnt exists in ", actual_path)

folder_cleanup2()

#Usecase2: I wanted to clean the tmp folder in a any input path C:\\dataset1\\tmp passed as an argument, if it exists

def folder_cleanup3(path_arg:str):
    actual_path=path_arg
    try:
         if os.path.exists(actual_path):
            shutil.rmtree(actual_path)
            print("Folder removed successfully from the path", actual_path)
         else:
             raise FileNotFoundError
    except FileNotFoundError as e:
            print("Folder remove failed due to folder doesnt exists in ", actual_path)

folder_cleanup3(input("Enter the path to be cleaned:")) #input:C:\\Users\\HP\\PycharmProjects\\WE47Usecases\\dataset1


#Usecase3: I wanted to clean the tmp folder in a given input path C:\\dataset1\\tmp,
# if it exists and return the status of True/False

def folder_cleanup4():
    actual_path="C:\\Users\\HP\\PycharmProjects\\WE47Usecases\\dataset1"
    try:
         if os.path.exists(actual_path):
            shutil.rmtree(actual_path)
            print("Folder remove successfully from the path", actual_path)
            return "Success"
         else:
             raise FileNotFoundError
    except FileNotFoundError as e:
            print("Folder remove failed due to folder doesnt exists in ", actual_path)
            return "Failed"
Status=folder_cleanup4()
print("The status of the folder removal process is:",Status)


#Usecase4: I wanted to clean any input folder in a given input path C:\\dataset1\\anything, if it exists and return the status
def folder_cleanup4(path_arg:str):
    actual_path=path_arg
    try:
         if os.path.exists(actual_path):
            shutil.rmtree(actual_path)
            print("Folder remove successfully from the path", actual_path)
            return "Success"
         else:
             raise FileNotFoundError
    except FileNotFoundError as e:
            print("Folder remove failed due to folder doesnt exists in ", actual_path)
            return "Failed"
Status=folder_cleanup4(input("Enter the path to be cleaned:"))
print("The status of the folder removal process is:",Status)


#Simple usecase (Strategic):
# a. Complete the Swiggy/zomato usecase (anonymous program) by creating a formal reusable method/function
# b. and add exception handling also in it..


#Usecase4 (reiterate):
# I wanted to clean any input folder in a given input path C:\\dataset1\\anything,
# if it exists and return the status,
# if the user is not passing the input path, then it has to be defaulted with tmp folder

def folder_cleanup5(folder_to_be_deleted:str='tmp1'):
    actual_path="C:\\Users\\HP\\PycharmProjects\\WE47Usecases\\dataset1\\"
    folder_path=actual_path+folder_to_be_deleted
    print("The folder path is:",folder_path)
    try:
         if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Folder {folder_to_be_deleted} remove successfully from the path {folder_path}")
            return "Success"
         else:
             raise FileNotFoundError
    except FileNotFoundError:
            print(f"Folder removal failed as {folder_to_be_deleted} folder doesnt exists in {actual_path}")
            return "Failed"
Status=folder_cleanup5()
print("The status of the folder removal process is:",Status)



#Usecase: I want to create a mail id for the users, users will give fname,lname & domain or only they give fname and lname
#requirement:
# if i call the above function with 3 arguments like fname,lname,domain then it should return fname.lname@domain.com
# if i call the above function with 2 arguments like fname,lname then it should return fname.lname@inceptez.com
# if i call the above function with 1 argument like fname then it should return fname.na@inceptez.com
#if no param is passed just print, minimum name is needed...

def generate_mail(**kwargs):
    print("type of arb argument is Dictionary",type(kwargs))
    print("value in the kwargs",kwargs)
    fname=kwargs['fname']
    lname = kwargs.get('lname','na')
    domain = kwargs.get('domain','inceptez.com')
    final_mail = fname + '.' + lname + '@' + domain
    return final_mail

generate_mail(fname='mohamed',lname='irfan',domain='cts.com')
generate_mail(lname='irfan',fname='mohamed',name='girish')
generate_mail(fname='mohamed',lname='irfan')
generate_mail(fname='mohamed')


#Usecase strategic (arb arg, default arg, arb keyword arg): Create a method to calculate sal+bonus+incentives for differenct IT companies using either arbitrary keyword arg function
#Hewitt/HRworkways..
#CTS, Infy, HCL calculate sal+bon+inc
# where CTS give all the 3 components
# Infy gives only first 2 components
# HCL gives only first 1 component
#We need to get the results as given below..
#calc_gross_sal(comp='CTS',sal=100000,bon=10,inc=5000) -> 115000
#calc_gross_sal(comp='INFY',sal=100000,bon=5) -> 105000
#calc_gross_sal(comp='HCL',sal=100000) -> 100000
#arb arg, default arg

#Using Kwargs
class InvalidCompanyError(Exception):
    pass
def calc_gross_sal(**kwargs):

    try:
        salary = kwargs['sal']
        company = kwargs['comp']
        bonus = kwargs.get('bon', 0)
        increment = kwargs.get('inc', 0)
        if company not in ['CTS','INFY','HCL']:
            raise InvalidCompanyError("Company not found")
        else:
            if company == 'CTS':
                return (salary + ((salary * bonus) / 100) + increment)
            if company == 'INFY':
                return (salary + ((salary * bonus) / 100))
            if company == 'HCL':
                return (salary)
    except TypeError as e:
        print(f"Enter a valid datatype for comp and sal.You have entered  salary as {salary}")

    except KeyError as e:
        print("It is required to provide the mandatory key value for", e)
    except InvalidCompanyError:
        print("Invalid company name",company,". You have entered a invalid company name. Enter 'CTS' or 'INFY' or 'HCL'")


salary_final=calc_gross_sal(sal=457893457,comp='CTS')
print(salary_final)

#calc_gross_sal('CTS',100000,10,5000) -> 115000
#calc_gross_sal('INFY',100000,5) -> 105000
#calc_gross_sal('HCL',100000) -> 100000

#Using arb args and default args

"""
class InvalidCompanyError(Exception):
    pass
def calc_gross_sal(*args,sal:int,bon:int=0,inc:int=0):
    print(args,sal,bon,inc)
    company=""
    try:
        for i in args:
            if i in ['CTS','INFY','HCL']:
                company=i
                break
        if not company:
                raise InvalidCompanyError("Company not found")
        salary = sal
        bonus = bon
        increment = inc
        print(company,salary,bonus,increment)
        if company == 'CTS':
            return (salary + ((salary * bonus) / 100) + increment)
        if company == 'INFY':
            return (salary + ((salary * bonus) / 100))
        if company == 'HCL':
            return (salary)
    except TypeError as e:
        print(f"Enter a valid datatype for comp and sal.You have entered  salary as {salary}")

    except KeyError as e:
        print("It is required to provide the mandatory key value for", e)
    except InvalidCompanyError:
        print("Invalid company name",company,". You have entered a invalid company name. Enter 'CTS' or 'INFY' or 'HCL'")

salary_final=calc_gross_sal('CTS','Velachery','tidelpark',sal=457893457)
print(salary_final)
"""