
def scramble(r_letters, s_letters):
    if len(r_letters) == 0:
        print(s_letters)
    else:
        for i in range(len(r_letters)):
            scramble_letter = r_letters[i]
            remaining_letters = r_letters[:i] + r_letters[i+1:]
            scramble(remaining_letters, s_letters + scramble_letter)

word = input('Enter a word to be scrambled: ')
scramble(word, '')
