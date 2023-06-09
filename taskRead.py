import csv

""" Here reading csv file using generator with the details about emplopyees such as name,id,age,designation ,mob_number
    And seperately creating csv files by age of below 25 and between 25&45
"""

def readCsvFile(file_name):
    with open(file_name,"r") as readFile:
        empDatas = csv.reader(readFile)
        next(empDatas)
        belowAge = []
        aboveAge = []
        for datas in empDatas:
            yield datas
            age = int(datas[2])
            if(age<25):
                belowAge.append(datas)
            elif(age>25 and age<45):
                aboveAge.append(datas)
        
        with open("Employee_Below_25_Data.csv","w",newline="") as file:
            belowAgeData = csv.writer(file)
            belowAgeData.writerows(belowAge)
        
        with open("Employee_Between_25_45_Data.csv","w",newline="") as file:
            aboveAgeData = csv.writer(file)
            aboveAgeData.writerows(aboveAge)
        

for data in readCsvFile("EmployeeDatas.csv"):
    for employee in data:
        print(employee)

