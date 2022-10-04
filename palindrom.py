def Palindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

slovo=input("napis mi slovko: ")
s=slovo.replace(" ","")
ans = Palindrome(s)

if(ans):
    print("slovko je palindrom")
else:
    print("slovko nieje palidrom")
