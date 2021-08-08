def SwapData():
    file1 = input("Enter File Name: ")
    with open(file1,'r') as a:
        data_a = a.read()
    with open(file1,'w') as a:
        a.write("i am bad")
SwapData()

def SwapData2():
    file2 = input("Enter File Name: ")
    with open(file2,'r') as a:
        data_a = a.read()
    with open(file2,'w') as a:
        a.write("i am good")
SwapData2()