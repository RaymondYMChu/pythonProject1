str1="Hello the world"

indexArr=[]
def checkChars(char):
    for index in range(0,len(str1)):
        if str1[index]==char:
            indexArr.append(index)
    print(indexArr)
checkChars("o")
