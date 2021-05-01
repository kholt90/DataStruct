
# You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.
# To do this, you'll need data.
# Write code that takes a long string and builds its word cloud data in a dictionary, where the keys are words and the values are the number of times the words occurred.
# Think about capitalized words.
# For example, look at these sentences:
# 'After beating the eggs, Dana read the next step:'
# 'Add milk and eggs, then add flour and sugar.'
# What do we want to do with "After", "Dana", and "add"?
# In this example, your final dictionary should include one "Add" or "add" with a value of 2.
# Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".
# Assume the input will only contain words and standard punctuation.
# You could make a reasonable argument to use regex in your solution.
# We won't, mainly because performance is difficult to measure and can get pretty bad.

print("\n-----===== Start =====-----\n")

def WordCloud(the_string):
    the_data = {}
    the_string = the_string.lower().split()
    for i in the_string:
        if i in the_data:
            the_data[i] = the_data[i] + 1
        else:
            the_data[i] = 1
    return the_data

long_string = "After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar."

print(f"The String: {WordCloud(long_string)}")

print("\n-----===== End =====-----")