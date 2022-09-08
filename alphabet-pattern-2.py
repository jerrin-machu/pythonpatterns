
n =5
string = ""
count = 0
for i in range(1,n+1):
    for j in range(0,i):
        string = string + chr(count+ 65)
        count = count + 1
    string = string + "\n"

print(string)