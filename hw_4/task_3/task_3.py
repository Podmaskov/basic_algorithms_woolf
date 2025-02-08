import timeit

# Knuth-Morris-Pratt algorithm
def compute_lps(pattern):
    """
    Computes the longest prefix-suffix (lps) array for the KMP algorithm.
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Performs Knuth-Morris-Pratt search on the given text for the given pattern.
    """
    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern
    indexes = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            indexes.append(i - len(pattern))
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    if indexes:
        print(f"Search with KMP algorithm: {indexes}")
    else:
        print(f"No matches found for '{pattern}'")

# Boyer-Moore algorithm
def build_shift_table(pattern):
    """
    Create a shift table for the Boyer-Moore algorithm.
    """
    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    """
    Performs Boyer-Moore search on the given text for the given pattern.
    """
    indexes = []
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            indexes.append(i)
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    if indexes:
        print(f"Search with Boyer-Moore algorithm: {indexes}")
    else:
        print(f"No matches found for '{pattern}'")

# Rabin-Karp algorithm
def polynomial_hash(s, base=256, modulus=101):
    """
    Returns the polynomial hash of string s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1, modulus)
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    """
    Performs Rabin-Karp search on the given text for the given substring.
    """
    substring_length = len(substring)
    main_string_length = len(main_string)
    indexes = []

    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1, modulus)

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                indexes.append(i)

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    if indexes:
        print(f"Search with Rabin-Karp algorithm: {indexes}")
    else:
        print(f"No matches found for '{substring}'")

article1 = "./hw_4/task_3/data/text_1.txt"
article2 = "./hw_4/task_3/data/text_2.txt"
pattern = "algorithms"

with open(article1, "r", encoding="utf-8") as file:
    text_1 = file.read()

with open(article2, "r", encoding="utf-8") as file:
    text_2 = file.read()

def compare_algorithms(string, pattern):
    """
    Compares the execution time of KMP, Boyer-Moore, and Rabin-Karp searches.
    """
    times = []
    times.append(("Knuth-Morris-Pratt algorithm", timeit.timeit(lambda: kmp_search(string, pattern), number=1)))
    times.append(("Boyer-Moore algorithm", timeit.timeit(lambda: boyer_moore_search(string, pattern), number=1)))
    times.append(("Rabin-Karp algorithm", timeit.timeit(lambda: rabin_karp_search(string, pattern), number=1)))

    print("Searching algorithms ranked by time:")
    for algo, time_taken in times:
        print(f"{algo}: {time_taken:.6f} seconds")

if __name__ == "__main__":
    print('------------------Test data 1-----------------------')
    compare_algorithms(text_1, pattern)
    print('------------------Test data 2-----------------------')
    compare_algorithms(text_2, pattern)