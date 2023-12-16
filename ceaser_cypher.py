alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)] * 2




game_is_on = True
def game(word, shift_amount):
    word_gen = ""
    if function_to_do == "decrypt":
        shift_amount *= -1
    for words in word:
        if words in alphabets:
            index = alphabets.index(words)
            word_gen += alphabets[index + shift_amount]

    print(word_gen)
        

while game_is_on:
    word = input("Enter a word: ").lower()
    shift_amount = int(input("Enter a shift number: "))
    function_to_do = input("Do you want to encrypt or decrypt? ").lower()
    game(word, shift_amount)

    should_continue = input("Do you want to continue? (y/n) ").lower()
    if should_continue == "n":
        game_is_on = False
        print("Thank you for cyphering the Word")
        break