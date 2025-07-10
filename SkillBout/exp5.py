with open("file.txt",'w') as file:
    file.write("Python ")
with open("file.txt",'a') as file:
    file.write("Java")
with open("file.txt",'r') as file:
    data=file.read()
    print(data)

