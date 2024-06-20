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

def process_queries(queries):
    processor = WordProcessor()
    results = []

    for query in queries:
        parts = query.split()
        command = int(parts[0])
        word = parts[1]

        if command == 1:
            processor.insert(word)
        elif command == 2:
            results.append(processor.search(word))
        elif command == 3:
            results.append(processor.starts_with(word))

    return results

# Test case input
queries_1 = [
    "1 school",
    "1 world",
    "1 word",
    "1 scholar",
    "2 word",
    "3 sch"
]

queries_2 = [
    "1 car",
    "1 cap",
    "2 ca",
    "3 ca",
    "1 can",
    "3 ca",
    "2 cap"
]

# Process queries
results_1 = process_queries(queries_1)
results_2 = process_queries(queries_2)

# Output results for test case 1
for result in results_1:
    print("TRUE" if result else "FALSE")

print()  # For separating the outputs of two test cases

# Output results for test case 2
for result in results_2:
    print("TRUE" if result else "FALSE")
