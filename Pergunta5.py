string = "hello world"
string_reversa = string 

for i in range(len(string)-1, -1, -1):
    string_reversa += string[i]
    
print(string_reversa) # saída: "dlrow olleh"