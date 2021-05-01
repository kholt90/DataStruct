
# You're working on a secret team solving coded transmissions.
# Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault.
# The message has been mostly deciphered, but all the words are backward! Your colleagues have handed off the last step to you.
# Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.
# Why a list of characters instead of a string?
# The goal of this question is to practice manipulating strings in place. Since we're modifying the message, we need a mutable type like a list, instead of Python's immutable strings.
# For example:
#     message = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]

# reverse_words(message)

# # Prints: 'steal pound cake'
# print ''.join(message)

# When writing your function, assume the message contains only letters and spaces, and all words are separated by one space.

print("\n-----===== Start =====-----\n")

def Reverse(the_list):
    for i in range(len(the_list) // 2):
        the_list[i], the_list[-(i + 1)] = the_list[-(i + 1)], the_list[i]
    return the_list

def ReverseWords(the_message):
    Reverse(the_message)
    word_start = 0
    for i, el in enumerate(the_message):
        if el == " ":
            the_message[word_start:i] = Reverse(the_message[word_start:i])
            word_start = i + 1
    the_message[word_start:] = Reverse(the_message[word_start:])
    return the_message

message = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]

print(f"The Backwards Message: {''.join(message)}")
print(f"The Real Message: {''.join(ReverseWords(message))}")

print("\n-----===== End =====-----")