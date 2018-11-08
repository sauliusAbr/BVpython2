#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# [ ] get user input for a variable named remind_me
remind_me=input("Enter time when to remind you: ")

# [ ] print the value of the variable remind_me
print(remind_me)


# In[ ]:


# use string addition to print "remember: " before the remind_me input string
print("remember "+remind_me)


# In[ ]:


# [ ] get user input for 2 variables: meeting_subject and meeting_time
meeting_subject=input("what is the meeting subject?: ")
meeting_time=input("what is the meeting time?: ")

# [ ] use string addition to print meeting subject and time with labels
print("Meeting Subject: "+meeting_subject)
print("Meeting time: "+meeting_time)


# In[ ]:


# [ ] print the combined strings "Wednesday is" and "in the middle of the week" 
print("Wednesday is","in the middle of the week")


# In[ ]:


# [ ] print combined string "Remember to" and the string variable remind_me from input above
print("Remember to",remind_me)


# In[ ]:


# [ ] Combine 3 variables from above with multiple strings
print("Wednesday is","in the middle of the week so","remember your stuff at",remind_me)


# In[ ]:


# [ ] print a string sentence that will display an Apostrophe (')
print("This can't fail")


# In[ ]:


# [ ] print a string sentence that will display a quote(") or quotes
print('"this can not fail"-Saulius')


# In[ ]:


# [ ] complete vehicle tests
vehicle=input("Enter vehicle ")
print("All Alpha:",vehicle.isalpha())
print("All Alpha and numeric:",vehicle.isalnum())
print("Is Capitalized:",vehicle.istitle())
print("All Lowercase:",vehicle.islower())


# In[ ]:


# [ ] print True or False if color starts with "b" 
color=input("Enter color: ")
print("Color starts with 'b'?",color.startswith('b'))


# In[ ]:


# [ ] print the string variable capital_this Capitalizing only the first letter
capitalize_this = "the TIME is Noon."
print(capitalize_this.upper())


# In[ ]:


# print the string variable swap_this in swapped case
swap_this = "wHO writes LIKE tHIS?"
print(swap_this.swapcase())


# In[ ]:


# print the string variable whisper_this in all lowercase
whisper_this = "Can you hear me?"
print(whisper_this.lower())


# In[ ]:


# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"
print(yell_this.upper())


# In[ ]:


# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"
print(yell_this.upper())


# In[ ]:


# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"
print(yell_this.upper())


# In[ ]:


# [ ] get user input for a variable named color
# [ ] modify color to be all lowercase and print
color=input("Enter color: ").lower()
print(color)


# In[ ]:


# [ ] get user input using variable remind_me and format to all **lowercase** and print
# [ ] test using input with mixed upper and lower cases
remind_me=input("Enter string: ").lower()
print(remind_me)


# In[ ]:


# [] get user input for the variable yell_this and format as a "YELL" to ALL CAPS
yell_this=input("what? ").upper()
print(yell_this)


# In[ ]:


# [ ] get user input for the name of some animals in the variable animals_input
animals_input=input("Enter animals: ").lower()

# [ ] print true or false if 'cat' is in the string variable animals_input
print("Is there a cat?",'cat' in animals_input)


# In[ ]:


# [ ] get user input for color
color=input("Enter color: ")

# [ ] print True or False for starts with "b"
print("Starts with 'b'?",color.startswith('b'))

# [ ] print color variable value exactly as input 
#     test with input: "Blue", "BLUE", "bLUE"
print(color)


# In[ ]:


# project: "guess what I'm reading"

# 1[ ] get 1 word input for can_read variable
can_read=input("Enter a 1 word thing that can be read: ")

# 2[ ] get 3 things input for can_read_things variable
can_read_things=input("Enter 3 things that can be read: ")

# 3[ ] print True if can_read is in can_read_things
print("Item found =",can_read in can_read_things)

# [] challenge: format the output to read "item found = True" (or false)
# hint: look print formatting exercises


# In[ ]:


# Allergy check 

# 1[ ] get input for test
input_test=input("Enter categories of food that you have eaten in the last 24 hours: ").lower()

# 2/3[ ] print True if "dairy" is in the input or False if not
print("Is dairy in the input?: ",'dairy' in input_test)


# 4[ ] Check if "nuts" are in the input
print("Are nuts in the input?: ",'nuts' in input_test)
# 4+[ ] Challenge: Check if "seafood" is in the input
print("Is seafood in the input?: ",'seafood' in input_test)
# 4+[ ] Challenge: Check if "chocolate" is in the input
print("Is chocolate in the input?: ",'chocolate' in input_test)


# In[ ]:




