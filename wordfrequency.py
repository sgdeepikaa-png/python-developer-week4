import string

filename = input("Enter file name (Press Enter for sample.txt): ")

if filename == "":
    filename = "sample.txt"

try:
    with open(filename, "r") as file:
        text = file.read()

except FileNotFoundError:
    print("File not found.")
    exit()

# Convert to lowercase
text = text.lower()

# Split words
words = text.split()

# Remove punctuation
cleaned = []

for word in words:
    word = word.strip(string.punctuation)
    if word != "":
        cleaned.append(word)

# Count frequency
freq = {}

for word in cleaned:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Sort
top = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 Words")
print("-------------------------")

for word, count in top[:10]:
    print(word, ":", count)