import string

ALPHABET = list(string.printable) 
occurencies = {}
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

for letter in ALPHABET:
    occurencies[letter] = 0

for char in text:
    occurencies[char]+=1.0

for key, value in occurencies.items():
    occurencies[key] = value/len(text)*100

sorted_occurencies = sorted(occurencies.items(), key=lambda x:x[1], reverse=True)

print(sorted_occurencies)
