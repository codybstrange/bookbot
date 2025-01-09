path_to_file = "books/frankenstein.txt"

def count_words(contents):
    return len(contents.split())

def get_report(path_to_file):
    print(f"--- Begin report of f{path_to_file} ---")
    contents = get_contents(path_to_file)
    word_count = count_words(contents)
    print(f"{word_count} words found in the document")
    print("")
    counts = count_chars(contents)
    counts = dict(sorted(counts.items(), reverse=True, key=lambda item: item[1]))
    for k in counts.keys():
        print(f"The '{k}' character was found {counts[k]} times")
    print("--- End report ---")
    return

def count_chars(contents):
    contents = contents.lower()
    count = {}
    for c in contents:
        if not c.isalpha():
            continue
        if c not in count.keys():
            count[c] = 1
        else:
            count[c] += 1
    return count

def get_contents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#print(file_contents)

get_report(path_to_file)
