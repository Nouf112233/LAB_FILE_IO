myFile=open("todoList.txt","w",encoding="utf-8")
myFile.writelines("l woke up at 8 am\n I learned recursion and lambda function\n I learned too python file I/O \n I study hard")
myFile=open("todoList.txt","r",encoding="utf-8")
content=myFile.read()
print(content)
