def find_longest(*words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(find_longest("cat", "elephant", "dog"))
