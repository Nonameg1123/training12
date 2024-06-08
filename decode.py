s=input().lower()
dec=int(input())
res=""
for i in s:
    t=(((ord(i)-97-dec)%26)+97)
    res+=chr(t)
print(res)