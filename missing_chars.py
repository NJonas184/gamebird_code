programming_languages = ["python", "java", "ruby", "c++", "swift"]

while True:
    input_word = input('enter word:').lower()
    if input_word == "!q":
        break # Break loop and end program

    found = False
    for language in programming_languages:
        if input_word == language:
            print('ok,', language)
            found = True
            break
        elif set(input_word).issubset(set(language)):
            missing_chars = language # Initialize missing_chars with all of language's characters
            for i in input_word:
                # Iterate through input_word characters
                missing_chars = missing_chars.replace(i, "", 1)
                # Remove each character in input_word from missing_chars
            print(f' no {input_word} there, maybe you mean, {language} (missing characters: {", ".join(missing_chars)})')
            found = True
            break

    if not found:
        print('no')
