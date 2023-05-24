import csv

def readCsvFile(file_name):
    with open(file_name,"r") as readFile:
        empDatas = csv.reader(readFile)
        next(empDatas)
        belowAge = []
        aboveAge = []
        for datas in empDatas:
            age = int(datas[2])
            if(age <= 25):
                belowAge.append(datas)
            elif(age>25 and age<45):
                aboveAge.append(datas)
        
        with open("EmployeeBelowData.csv","w",newline="") as file:
            belowAgeData = csv.writer(file)
            belowAgeData.writerows(belowAge)
        
        with open("EmployeeAboveData.csv","w",newline="") as file:
            aboveAgeData = csv.writer(file)
            aboveAgeData.writerows(aboveAge)
        
        yield belowAge
        yield aboveAge

for data in readCsvFile("EmployeeDatas.csv"):
    for employee in data:
        print(employee)

