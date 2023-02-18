from collections import deque

vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]

flowers_dict = {"rose": "rose",
                "tulip": "tulip",
                "lotus": "lotus",
                "daffodil": "daffodil"}
word_found = False
found_word_list = None
while vowels and consonants and not word_found:
    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()
    for pair in flowers_dict.items():
        flora = pair[0]
        mirror = pair[1]

        if first_vowel in flora:
            mirror = mirror.replace(first_vowel, "")
            flowers_dict[flora] = mirror
        if last_consonant in flora:
            mirror = mirror.replace(last_consonant, "")
            flowers_dict[flora] = mirror
        if not flowers_dict[flora]:
            word_found = True
            found_word_list = flora
            break

if not word_found:
    print("Cannot find any word!")
else:
    print(f"Word found: {found_word_list}")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")



# from collections import deque
#
# vowels = deque(x for x in input().split())
# consonants = [x for x in input().split()]
#
# flowers_dict = {"rose": "",
#                 "tulip": "",
#                 "lotus": "",
#                 "daffodil": ""}
# word_found = False
# found_word_list = None
# while vowels and consonants and not word_found:
#     first_vowel = vowels.popleft()
#     last_consonant = consonants.pop()
#     for pair in flowers_dict.items():
#         flora = pair[0]
#         letters = pair[1]
#         if first_vowel in flora and first_vowel not in letters:
#             flowers_dict[flora] += first_vowel
#         if last_consonant in flora and last_consonant not in letters:
#             flowers_dict[flora] += last_consonant
#         if len(flora) == len(flowers_dict[flora]):
#             word_found = True
#             found_word_list = flora
#             # vowels.appendleft(first_vowel)
#             # consonants.append(last_consonant)
#             break
#
# if not word_found:
#     print("Cannot find any word!")
# else:
#     print(f"Word found: {found_word_list}")
#
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")