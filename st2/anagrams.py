import fileinput

def main():
    anagrams = {}
    for line in fileinput.input("wordlist.txt"):
        line = line.strip()
        if line:
            sortedline = "".join(sorted(line))
            anagrams[sortedline] = anagrams.get(sortedline, []) + [line]

    with open("anagrams.txt", "w") as output_file:
        i = 1
        for key in anagrams:
            if len(anagrams[key]) > 1:
                words = ", ".join(anagrams[key])
                print("Anagram %s:" % i, words, file=output_file)
                i += 1

if __name__ == "__main__":
    main()


