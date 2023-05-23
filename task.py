def readCsvFile(file_name):
    with open(file_name,"w+") as file:
        file.write("Employee Id,Employee Name,Employee Age,Designation,Contact Number\nEmp1,Vinoth,23,Fluter Developer,3453443784\nEmp2,Navin,22,React Developer,6363788932\nEmp3,Athiyaman,23,Python Developer,7373456782\nEmp4,Sachin,20,Fluter Developer,7363456432\nEmp5,Saran,21,Python Developer,9344291466\nEmp6,Poovarasan,27,Senior Developer,7341576892\nEmp7,Murali,42,GM,9561345289\nEmp8,Manikandan,48,PDM,8765785620\nEmp9,Lakshmi,27,Python Senior Developer,9786786549\nEmp10,Gokul,30,DotNet,7356876599\nEmp11,Daya,29,Team Lead,7898775659\nEmp12,Sarath,28,React Senior Developer,6789654470")
        for data in readCsvFile(file_name):
            if(data[2] > "25" and data[2] < "45"):
                yield 
    # with open(file_name,"r") as file:
    #         print(file.read())



readCsvFile("EmployeeDatas.csv")


