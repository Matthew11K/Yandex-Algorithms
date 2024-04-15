def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return "NO"

    count_str1 = {}
    count_str2 = {}

    for char in str1:
        count_str1[char] = count_str1.get(char, 0) + 1

    for char in str2:
        count_str2[char] = count_str2.get(char, 0) + 1

    return "YES" if count_str1 == count_str2 else "NO"

str1 = input()
str2 = input()

print(are_anagrams(str1, str2))
