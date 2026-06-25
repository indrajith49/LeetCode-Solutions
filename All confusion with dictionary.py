# COUNTING (Anagram)
count = {}
for char in "aab":
    count[char] = count.get(char, 0) + 1
print(count)  # {'a': 2, 'b': 1}
              #  ↑     ↑
              # char  count

# INDEXES (Longest Substring)
last_seen = {}
for i, char in enumerate("abcabcbb"):
    last_seen[char] = i
print(last_seen)  # {'a': 3, 'b': 7, 'c': 5}
                  #  ↑     ↑
                  # char  index

"""
The Same Dictionary Can Do Two Different Things:
What it stores	Example	Use Case
Counts	{'a': 2, 'b': 1}	"How many times?"
Indexes	{'a': 0, 'b': 1}	"Where was it last seen?"
Same dictionary structure, DIFFERENT meaning.

"""


What a Dictionary Can Store:
Use Case	What It Stores	Example
1. Counts	How many times	{'a': 2, 'b': 1}
2. Last Index	Where seen last	{'a': 3, 'b': 7}
3. Mapping	Key → Value (anything!)	{1: 'one', 2: 'two'}
4. Grouping	Group similar items	{'aet': ['eat','tea']}
5. Cache/Memoization	Store computed results	{5: 120, 4: 24}
6. Lookup Table	Fast existence check	{'apple': True, 'banana': True}
1. Counting Frequencies (You Know This)
python
# Count occurrences
count = {}
for char in "hello":
    count[char] = count.get(char, 0) + 1
print(count)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
2. Storing Last Index (You Know This)
python
# Store last position
last_seen = {}
for i, char in enumerate("abcabc"):
    last_seen[char] = i
print(last_seen)  # {'a': 3, 'b': 4, 'c': 5}
3. Mapping (Key → Value)
python
# Phone book
phone_book = {
    "Alice": "123-4567",
    "Bob": "234-5678",
    "Charlie": "345-6789"
}
print(phone_book["Alice"])  # "123-4567"
4. Grouping (Group Anagrams)
python
# Group by sorted string
result = {}
for word in ["eat", "tea", "tan", "ate"]:
    sorted_word = ''.join(sorted(word))
    if sorted_word in result:
        result[sorted_word].append(word)
    else:
        result[sorted_word] = [word]
print(result)  # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan']}
5. Cache/Memoization (Fibonacci)
python
# Store computed results to avoid recalculating
cache = {}
def fib(n):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

print(fib(10))  # 55
6. Lookup Table (Fast Checking)
python
# Store allowed values
valid_emails = {
    "alice@email.com": True,
    "bob@email.com": True,
    "charlie@email.com": True
}
print("alice@email.com" in valid_emails)  # True
print("hacker@email.com" in valid_emails)  # False
7. Prefix Sum (Subarray Sum)
python
# Store prefix sums
prefix_sum = {0: 1}  # sum: count
current_sum = 0
for num in [1, 2, 3]:
    current_sum += num
    prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
print(prefix_sum)  # {0: 1, 1: 1, 3: 1, 6: 1}
8. Storing Multiple Values (Lists as Values)
python
# Store list of values per key
student_courses = {
    "Alice": ["Math", "Physics"],
    "Bob": ["Chemistry", "Biology"]
}
student_courses["Alice"].append("CS")
print(student_courses)  # {'Alice': ['Math', 'Physics', 'CS'], ...}
9. Storing Nested Dictionaries
python
# Store dictionary inside dictionary
users = {
    "alice": {"age": 25, "city": "NY", "job": "Engineer"},
    "bob": {"age": 30, "city": "LA", "job": "Designer"}
}
print(users["alice"]["city"])  # "NY"
Summary Table:
Use Case	Code Example	What It Stores
Count	count[char] = count.get(char, 0) + 1	Numbers (counts)
Last Index	seen[char] = right	Numbers (indexes)
Mapping	phone_book["Alice"] = "123-4567"	Any value
Grouping	groups[sorted_word].append(word)	Lists
Cache	cache[n] = fib(n-1) + fib(n-2)	Numbers
Lookup	valid[email] = True	Boolean
Prefix Sum	prefix_sum[current_sum] = count	Numbers
Nested	users["alice"]["city"] = "NY"	Dictionaries
The Most Important Thing:
Dictionary = Key → Value Mapping

Key	Value
Can be any immutable type (string, int, tuple)	Can be ANYTHING (string, int, list, dict, object)
Unique	Can be anything
Quick Reference:
python
# Creating a dictionary
d = {}
d = {"name": "Alice", "age": 25}
d = dict(name="Alice", age=25)

# Adding/Updating
d[key] = value

# Getting value
d.get(key, default)

# Checking existence
if key in d:

# Removing
del d[key]
d.pop(key)

# Looping
for key in d:
for key, value in d.items():
