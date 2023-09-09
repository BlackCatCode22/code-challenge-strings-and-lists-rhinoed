## Check List for Code Challenge Strings and Lists

### Strings
```python
str_one = " The quick brown fox jumps over the lazy dog. "
str_two = "The slow black dog bows before the regal fox."
```
#### Operations

###### Remove Spaces
- [x] Create variable `str_no_spaces`
- [x] Use `strip()` to remove leading and trailing spaces from `str_one` store in `str_no_spaces`
- [x] Use `replace(" ", """)`to remove all spaces from `str_no_spaces`
- [x] Output `str_no_spaces` in `print("\n str_no_spaces is..." + str_no_spaces)`

###### Concatenation
- [x] Create variable `str_cat` that stores `str_one + str_two`
- [x] Output `str_cat` in `print("\n str_cat is... " + str_cat)`

###### String Length
- [x] Use `len(str_cat)` to store length in variable `str_len`
- [x] Output `str_len` in `print("\n The length of " + str_cat + " is: " + str_len)`

###### String Lower
- [x] Store `str_cat.lower()` in variable named `str_cat_lower`
- [x] Output `str_cat_lower` in `print("\n str_cat_lower in lower case is: " + str_cat_lower)`

###### String Upper
- [x] Store `str_cat.upper()` in variable named `str_cat_upper`
- [x] Output `str_cat_upper` in `print("\n str_cat_upper in upper case is: " + str_cat_upper)`

```python
adjective = "smart"
verb = "ran"
preposition = "through"
```
###### Formatted String
- [x] Create `str_formatted = f"The {adjective} brown fox {ran} {preposition} the lazy dog"`
- [x] Output `str_formatted` in `print("\n str_formatted is: " + str_formatted)`

###### String Index
- [x] Store `str_two.find("black dog")` in variable `start_index`
- [x] Output `start_index` in `print("\n start_index is: " + start_index)`

###### String Slice
-[x] Create variable `substring_length = len("black dog")`
-[x] Extract "black dog" from `str_two` and store in variable `substring` using `substring = str_two[start_index :start_index + substring_length]`
-[x] Output `substring` in `print("\n substring is: " + substring)`
----
### Lists

```python
str_for_list = "Natalia, Alice, Bob, Charlie, Sergei, David, Eve, Frank, Grace, Dmitri, Hannah,Isaac, Jack, Ivan,, Olga"

```
###### List of Names
-[x] Create `list_of_names` variable using`list_of_names = str_for_list. split(", ")`
-[x] Output `list_of_names` using `print("\n list_of_names is: " + str(list_of_names))`

###### List Sorted
-[x] Create `list_sorted` variable using `list_sorted = sorted(list_of_names.copy())`
- [x] Output `list_sorted` using `print("\n list_sorted is: " + str(list_sorted))`

###### List Reversed
-[x] Create `list_reversed` variable using `list_reversed = list_sorted.copy()[::-1]`
- [x] Output `list_reversed` using `print("\n list_reversed is: " + str(list_reversed))`

###### For name in list
- [x] Output header using `print("For name In")`
-[x] Create `for` loop that iterates through `list_reversed` and outputs each name in `list_reversed` using `print("\n" + name)`

###### First Three
- [x] Use slice on list_sorted to create `first_three` using `first_three = list_sorted[:3]`
- [x] Output `first_three` using `print(first_three)`
- [x] Output `type(first_three)` using `print(str(type(first_three)))`

###### Modify List
- [x] Append Yevgeny and Svetlana to `list_sorted` using `list_sorted.append("Yevgeny")` and `list_sorted.append("Svetlana")`
- [x] Insert Boris into `list_sorted` using `list_sorted.insert(5, "Boris")`
- [x] Output `list_sorted` using `print("\n" + str(list_sorted))`

###### Extend List
- [x] Use extend to add first_three to list_sorted using `list_sorted.extend(first_three)`
- [x] Output `list_sorted` using `print("\n List extended: " + str(list_sorted))`

###### Resort List
- [x] Sort list_sorted in place using `list_sorted.sort()`
- [x] Output `list_sorted` using `print("\n List re-sorted: " + str(list_sorted))` 

###### Remove Alice
- [x] Remove Alice from `list_sorted` using `list_sorted.remove("Alice")`
- [x] Output `list_sorted` using `print("\n Alice removed: " + str(list_sorted))`

###### Remove Duplicate
- [x] Convert`list_sorted` to set then Revert `list_sorted` back to a list using `list_sorted = list(set(list_sorted))`
- [x] Output `list_sorted` using `print("\n Duplicates removed and sorted: " + str(list_sorted))`