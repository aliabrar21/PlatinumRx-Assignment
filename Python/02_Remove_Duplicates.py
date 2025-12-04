def remove_duplicates(text):
    result = ""
    for char in text:
        if char not in result:
            result += char
    return result


# Test cases
print(remove_duplicates("hello world"))
print(remove_duplicates("malayalam"))
print(remove_duplicates("apple"))