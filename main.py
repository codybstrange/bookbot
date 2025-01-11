import matplotlib.pyplot as plt
import numpy as np
import re
from os.path import join

import random as r
import numpy as np
import string

path_to_file = "books/frankenstein.txt"

def count_words(contents):
    return len(contents.split())

def get_word_dict(contents):
    contents = contents.lower()
    words = re.findall(r"\b\w+(?:[-']\w+)*\b", contents)
    count = {}
    for w in words:
        if w not in count.keys():
            count[w] = 1
        else:
            count[w] += 1
    
    return count

# Zipf wasn't the first to discover Zipf's law, but we'll stick with the convention
# of calling it that
def plot_zipfs_law(books):
    fig, ax = plt.subplots(1, figsize=(16, 9))
    fig_norm, ax_norm = plt.subplots(1, figsize=(16,9))
    for book_name, path_to_file in books.items():
        counts = get_ordered_counts(path_to_file)
        vals = list(counts.values())
        x = [i+1 for i in range(len(vals))]
        ax.plot(x, vals, label= book_name)
        total_count = sum(vals)
        vals_norm = [v/total_count for v in vals]
        ax_norm.plot(x, vals_norm, label=book_name)
    ax.legend()
    ax.set_yscale("log")
    ax.set_ylabel("Occurences")
    ax.set_xscale("log")
    ax.set_xticks([])
    ax.set_xlabel("Word Rank")
    fig.savefig("counts.png", dpi=450, bbox_inches="tight")     
    ax_norm.legend()
    ax_norm.set_yscale("log")
    ax_norm.set_ylabel("Normalized Frequency")
    ax_norm.set_xscale("log")
    ax_norm.set_xticks([])
    ax_norm.set_xlabel("Word Rank")
    fig_norm.savefig("counts_norm.png", dpi=450, bbox_inches="tight")     
    

def gen_random_text(num_words):
    s = ""
    for i in range(num_words):
        s += f"{gen_random_word()}"
        if i != num_words - 1:
            s += " "
    return s


def gen_random_word():
    # Using: https://www.sciencedirect.com/science/article/abs/pii/0378375886901692
    # Words in the English language are well-described by a Possion distribution
    # With "mean and variance equal to 6.94 and 5.80"
    word_length = np.random.poisson(6.94)
    s = ""
    for i in range(word_length):
        s += r.choice(string.ascii_letters)
    return s
    

def get_ordered_counts(path_to_file):
    contents = get_contents(path_to_file)
    counts = get_word_dict(contents)
    
    counts = dict(sorted(counts.items(), reverse=True, key=lambda item: item[1]))
    return counts

def get_char_report(path_to_file):
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
book_dir = "books"
books = {"Frankenstein": join(book_dir, "frankenstein.txt"), "Moby Dick": join(book_dir, "moby-dick.txt"), "War & Peace (EN)": join(book_dir, "war-and-peace.txt"), "Siddartha (DE)": join(book_dir, "siddartha_de.txt"), "Siddartha (EN)": join(book_dir, "siddartha_en.txt")}
#plot_zipfs_law(books)

books = {}
for i in range(10):
    n = np.random.poisson(50000)
    text = gen_random_text(n)
    text_path = join(book_dir, f"random_text_{i}.txt")
    with open(text_path, "w") as f:
        f.write(text)
    books[i] = text_path
plot_zipfs_law(books)
#get_char_report(path_to_file)
