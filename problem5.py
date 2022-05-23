start = 0
length = 1
maxLen = 1
s=input("enter any string : ")
for i in range(len(s)-1):
    if s[i+1] > s[i]:
            length += 1
    else:
            length = 1
    if length > maxLen:
            maxLen = length
            start = i + 2 - maxLen
print('Longest substring in alphabetical order is: '+ s[start : start + maxLen])