n= 6;
string = ""
for i in range(0,n):
    for j in range(0,i+1):
        if(i == 0 or i == n-1):
            string = string + "*"
        else:
            if j == 0 or j == i :
                string = string + "*"
            else:
                string = string + " "
    string = string + "\n"
    

print(string)