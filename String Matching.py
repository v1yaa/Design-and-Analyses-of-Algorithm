def string_matching(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break
    return result
words = ["mass", "as", "hero", "superhero"]
output = string_matching(words)
print(f"Words that are substrings of another word: {output}")
