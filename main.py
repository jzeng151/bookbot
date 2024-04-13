def main():
    with open("books/frankenstein.txt") as f:
        book_text = f.read()
        words = book_text.split()
    letter_count = count_letters(book_text)
    print_analysis(letter_count, len(words))

def count_letters(string):
    #converts entire book into lowercase 
    lowercase_string = string.lower()
    letter_count = {}
    #stores occurances of letters into a dictionary
    for letter in lowercase_string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

#takes a dictionary where key is letter and value is number of occurances
def print_analysis(dict, word_count):
    #convert letters in dictionary into list
    letters = []
    for item in dict:
        if item.isalpha():
            letters.append({"letter": item, "count": dict[item]})
    #sort list in descending order by number of occurances
    letters.sort(reverse=True, key=sort_with)
    #print analysis to console
    print("------ Report of frankenstein.txt ------")
    print(f"\n{word_count} words found in the document\n")
    for item in letters:
        print(f"The letter '{item["letter"]}' was found {item["count"]} times")
    print("\n----- End of Report -----")

def sort_with(dict):
    return dict["count"]

main()