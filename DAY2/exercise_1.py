import string

def word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()

    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

text = "Hello My name is Wasi and i am learning Python. Python is great!"
print(word_frequency(text))

result = word_frequency(text)

top_words = sorted(result.items(), key=lambda x: x[1], reverse=True)

# Print the top 5 most common words
for word, count in top_words[:5]:
    print(word, count)