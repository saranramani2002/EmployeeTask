import csv
import json

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



def convertAboveFile(csvFileName):
    with open(csvFileName,"r") as file:
        empdata = csv.reader(file)
        next(empdata)
        EmployeeDetail = []
        for data in empdata:
            # if(data[2]>"25" and data[2]<"45"):
            EmployeeDetail.append({"Employee Id":data[0],"Employee Name":data[1],"Employee Age":data[2],"Designation":data[3],"Contact Number":data[4]})
            with open("EmployeeAboveData.json","w") as file1:
                json.dump(EmployeeDetail,file1,indent=4)

convertAboveFile("EmployeeAboveData.csv")



def convertBelowAge(fileName):
    with open(fileName,"r") as belowFile:
        empdata1 = csv.reader(belowFile)
        next(empdata1)
        EmployeeDetail = []
        for data in empdata1:
            # a = data[2]
            # b = "25"
            # if (a<=b):
            EmployeeDetail.append({"Employee Id":data[0],"Employee Name":data[1],"Employee Age":data[2],"Designation":data[3],"Contact Number":data[4]})
            with open("EmployeeBelowData.json","w") as file1:
                json.dump(EmployeeDetail,file1,indent=4)

convertBelowAge("EmployeeBelowData.csv")