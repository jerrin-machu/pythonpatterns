n = 5
string =""
for i in range(1,n+1):
    for j in range(0,n-i+1):
        string = string + chr(j + 65)
    string = string + "\n"

print(string)