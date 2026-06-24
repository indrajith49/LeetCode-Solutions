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
