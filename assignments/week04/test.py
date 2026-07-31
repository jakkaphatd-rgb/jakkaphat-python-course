# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว (a, e, i, o, u)
# โดยใช้ loop-for ได้เท่่านั้น

# ตัวอย่างหน้าจอ
# whgat is your name?: Jakkaphat
# Your text have 4 vowels.

name = input("what is your name?")
""" letters = list("name")
print(letters)
 
a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')
 
A = letters.count('A')
E = letters.count('E')
I = letters.count('I')
O = letters.count('O')
U = letters.count('U')
 
count = a + e + i + o + u + A + E + I + O + U
"""
 
#Andy
 
count = 0
for letter in name:
    if letter == 'a' or letter 'A':
        count = count + 1
    if letter == 'e' or letter 'E':
        count = count + 1
    if letter == 'i' or letter 'I':
        count = count + 1
    if letter == 'o' or letter 'O':
        count = count + 1
    if letter == 'u' or letter 'U':
            count = count + 1
 
count = 0
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', "u"]:
            count = count + 1
         
   
 
#print("Your text have", count, "vowels")
has context menu