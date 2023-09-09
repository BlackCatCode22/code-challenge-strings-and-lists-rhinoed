# Code Challenge - Strings and Lists
# listExample01.py 9/1/23
#
# Python file name: strings_lists_CC_rhinoed.py
#
# Date: September 6, 2023
#
# Programmer's name: Mark Edmunds

# ********************************************************************************************
# Part 1 Strings

# String Constants
str_one = " The quick brown fox jumps over the lazy dog. "
str_two = "The slow   black dog bows before the regal fox."

# Remove Spaces
str_no_spaces = ""
str_no_spaces += str_one.strip()
str_no_spaces = str_no_spaces.replace(" ", "")
print("\n str_no_spaces is..." + str_no_spaces)

# Concatenation
str_cat = str_one.strip() + str_two.replace("   ", " ")
print("\n str_cat is... " + str_cat)

# String Length
str_len = len(str_cat)
print("\n The length of " + str_cat + " is: " + str(str_len))

# String Lower
str_cat_lower = str_cat.lower()
print("\n str_cat_lower in lower case is: " + str_cat_lower)

# String Upper
str_cat_upper = str_cat.upper()
print("\n str_cat_upper in upper case is: " + str_cat_upper)

# FormattedString Variables
adjective = "smart"
verb = "ran"
preposition = "through"

# Formatted String
str_formatted = f"The {adjective} brown fox {verb} {preposition} the lazy dog"
print("\n str_formatted is: " + str_formatted)

# String Index
start_index = str_two.find("black dog")
print("\n start_index is: " + str(start_index))

# String Slice
substring_length = len("black dog")
substring = str_two[start_index:start_index + substring_length]
print("\n substring is: " + substring)

# Part 2 Lists

# String for lists
str_for_list = "Natalia, Alice, Bob, Charlie, Sergei, David, Eve, Frank, Grace, Dmitri, Hannah,Isaac, Jack, Ivan,, Olga"

# List of Names
list_of_names = str_for_list. split(", ")
print("\n list_of_names is: " + str(list_of_names))

# List Sorted
list_sorted = sorted(list_of_names.copy())
print("\n list_sorted is: " + str(list_sorted))

# List Reversed
list_reversed = list_sorted.copy()[::-1]
print("\n list_reversed is: " + str(list_reversed))

# For name in list
# header
print("\n For name In list_reversed:")
# for loop
for name in list_reversed:
    print("\n" + name)

# First Three
first_three = list_sorted[:3]
print("\n The first three are: " + str(first_three))
print("\n type of first_three is: " + str(type(first_three)))

# Modify List
list_sorted.append("Yevgeny")
list_sorted.append("Svetlana")
list_sorted.insert(5, "Boris")
print("\n The modified list is: " + str(list_sorted))

# Extend List
list_sorted.extend(first_three)
print("\n List extended: " + str(list_sorted))

# Resort List
list_sorted.sort()
print("\n List re-sorted: " + str(list_sorted))

# Remove Alice
list_sorted.remove("Alice")
print("\n Alice removed List: " + str(list_sorted))

# Remove Duplicate
list_sorted = list(set(list_sorted))
list_sorted.sort()
print("\n Duplicates removed and sorted: " + str(list_sorted))





