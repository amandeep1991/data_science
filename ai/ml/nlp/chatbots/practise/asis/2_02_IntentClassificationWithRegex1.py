# Define a dictionary of patterns
patterns = {}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    # print('|'.join(keys))
    patterns[intent] = re.compile('|'.join(keys))

# Print the patterns
print(patterns)