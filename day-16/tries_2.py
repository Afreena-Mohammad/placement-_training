class WordProcessor:
    def __init__(self):
        self.words = set()

    def insert(self, word):
        self.words.add(word)

    def search(self, word):
        return word in self.words

    def starts_with(self, prefix):
        for word in self.words:
            if word.startswith(prefix):
                return True
        return False

# Read number of queries
n = int(input())

# Initialize the WordProcessor
processor = WordProcessor()

# Read and process each query
a = []
for i in range(n):
    item = input()
    a.append(item)

results = []
for item in a:
    command = int(item.split()[0])
    word = item.split()[1]

    if command == 1:
        processor.insert(word)
    elif command == 2:
        results.append(processor.search(word))
    elif command == 3:
        results.append(processor.starts_with(word))

# Output results
for result in results:
    print("TRUE" if result else "FALSE")
