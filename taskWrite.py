
""" Here creating csv file with the details about emplopyees such as name,id,age,designation ,mob_number """

import csv

details = (
    ("Employee Id","Employee Name","Employee Age","Designation","Contact Number"),
    ("Emp1","Vinoth","23","Fluter Developer","7345344378"),
    ("Emp2","Daya","29","Team Lead","7898775659"),
    ("Emp3","Navin","22","React Developer","6363788932"),
    ("Emp4","Murali","42","GM","9561345289"),
    ("Emp5","Athiyaman","23","Python Developer","7373456782"),
    ("Emp6","Sachin","20","Fluter Developer","7363456432"),
    ("Emp7","Saran","21","Python Developer","9344291466"),
    ("Emp8","Poovarasan","27","Senior Developer","7341576892"),
    ("Emp9","Manikandan","48","PDM","8765785620"),
    ("Emp10","Lakshmi","27","Python Senior Developer","9786786549"),
    ("Emp11","Gokul","30","DotNet","7356876599"),
    ("Emp12","Sarath","28","React Senior Developer","6789654470")
)

def writeCsvFile(file_name,data):
    with open(file_name,"w",newline="") as file:
        empData = csv.writer(file)
        empData.writerows(data)

writeCsvFile("EmployeeDatas.csv",details)