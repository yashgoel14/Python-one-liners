s = "yash"
t = "Ybrh"

if len(s)!=len(t):
    print("not equal")
else:
    for i in range(len(s)):
        s1 = ord(s[i])%(10**(len(s)-5))
        s2 = ord(t[i])%(10**(len(s)-5))
    if s1 == s2:
        print("anagram")
