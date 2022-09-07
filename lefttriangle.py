n = 5
string = ""
for i in range(1, n+1):
    for j in range(0, i):
        string = string + "*"
    string = string + "\n"

print (string)