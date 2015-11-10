def DashInsert(str):
    new_ = []    
    for i in range(len(str)):
        if int(str[i]) % 2 != 0 and int(str[i - 1]) % 2 != 0:
            if len(new_)>0:
                new_.append('-')
        new_.append(str[i])
    return "".join(new_)
print (DashInsert("454793"))


