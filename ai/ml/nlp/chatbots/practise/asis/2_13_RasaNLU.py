# Create the document
doc = nlp("let's see that jacket in red and some blue jeans")


# Iterate over parents in parse tree until an item entity is found
def find_parent_item(word):
    print("2nd loop: " + str(word))

    # Iterate over the word's ancestors
    for parent in word.ancestors:
        print("3rd loop(ancestors): " + str(parent))
        # Check for an "item" entity
        if entity_type(parent) == "item":
            return parent.text
    return None


# For all color entities, find their parent item
def assign_colors(doc):
    # Iterate over the document
    for word in doc:
        # Check for "color" entities
        print("1st loop: " + str(word))
        if entity_type(word) == "color":
            # Find the parent
            item = find_parent_item(word)
            print("item: {0} has color : {1}".format(item, word))


# Assign the colors
assign_colors(doc)
