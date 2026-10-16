#STRING LENGTH:
STR = "python"
print(len(STR)) 
student_names = ("Ravi","Charan","Rukmini","Satyabhama")
#Length for all the elements in the variable:
print(len(student_names)) 
# It will give individual length of string in the variable:
print(len(student_names[0]))
print(len(student_names[2])) 
# It also individual string length but all the elements output will be appeared at a time: 
print([len(name) for name in student_names]) 


# STRING METHODS:

Name = "Krishna"
print(Name.lower())
print(Name.upper())
print(Name.replace("K","S"))
print(Name.replace("Krishna","Shyam"))
Name1 = ".....Radha......"
print(Name1.lstrip("."))
print(Name1.rstrip("."))
print(Name1.strip(".")) 


# ESCAPE Sequences:
# 1) \n = New line
print("Hello\nworld")
print("------------------------------------")

# 2) \b = Back_space(It moves the cursor on step back)
str1 ="Helll\bo World"
print(str1)
print("------------------------------------")

# 3) \r = It will overwrites the characters(The cursor moves to the beginning):
text = "Ram\rTeja"
print(text)
print("------------------------------------")

# 4) \t = tab(Which gives space):
Info = "Name:\tRaghava\nStudy:\tB.Tech\nBranch:\tCSE AI/ML"
print(Info)
print("------------------------------------")

# 5) \'
str2 = "It\'s a sunny day"
print(str2)
print("------------------------------------")

# 6) \"
str3 = "Hasini is a \"GOOD girl!\""
print(str3)
print("------------------------------------")

# 7) \\ = Backslash


