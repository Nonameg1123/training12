a=input()
s=""
for i in a:
    if i.isalpha():
        if i in "aeiouAEIOU":
            s+=i.upper()
        else:
            s+=i.lower()
print(s)