import csv
import json

""" Here we convert csv file as json file using csv and json modules
    converting total employees detail """

def convertFile(csvFileName):
    with open(csvFileName,"r") as file:
        empdata = csv.reader(file)
        next(empdata)
        EmployeeDetail = []
        for data in empdata:
            EmployeeDetail.append({"Employee Id":data[0],"Employee Name":data[1],"Employee Age":data[2],"Designation":data[3],"Contact Number":data[4]})
        with open("EmployeeData.json","w") as file1:
            json.dump(EmployeeDetail,file1,indent=4)

convertFile("EmployeeDatas.csv")


""" Here we convert csv file as json file using csv and json modules
    converting below 25 age employees detail """

def convertBelowAge(fileName):
    with open(fileName,"r") as belowFile:
        empBelowData = csv.reader(belowFile)
        EmployeeDetail = []
        for data in empBelowData:
            EmployeeDetail.append({"Employee Id":data[0],"Employee Name":data[1],"Employee Age":data[2],"Designation":data[3],"Contact Number":data[4]})
            with open("EmployeeBelowData.json","w") as file1:
                json.dump(EmployeeDetail,file1,indent=4)

convertBelowAge("Employee_Below_25_Data.csv")



""" Here we convert csv file as json file using csv and json modules
    converting between 25 and 45 age employees detail """


def convertAboveFile(csvFileName):
    with open(csvFileName,"r") as file:
        empAboveData = csv.reader(file)
        EmployeeDetail = []
        for data in empAboveData:
            EmployeeDetail.append({"Employee Id":data[0],"Employee Name":data[1],"Employee Age":data[2],"Designation":data[3],"Contact Number":data[4]})
            with open("EmployeeAboveData.json","w") as file1:
                json.dump(EmployeeDetail,file1,indent=4)

convertAboveFile("Employee_Between_25_45_Data.csv")