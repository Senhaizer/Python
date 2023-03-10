def poem_vowels_count(testing_poem: list, checking_alfabet: set()) -> tuple[int]:
    list_of_vowels_number = []
    for i in range(len(testing_poem)):
        frase_vowels_number = int()
        for j in range(len(checking_alfabet)):
            frase = testing_poem[i]
            count = sum(map(lambda frase: 1 if checking_alfabet[j] in frase else 0, frase))
            frase_vowels_number += count
        list_of_vowels_number.append(frase_vowels_number)
    result = list_of_vowels_number
    return result
message_for_user_1 = 'Введите стихотворение: '
message_for_user_2 = 'Парам пам-пам'
message_for_user_3 = 'Пам парам'
alfabet_vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
poem = input(message_for_user_1).split(' ')
result = poem_vowels_count(testing_poem = poem, checking_alfabet = alfabet_vowels)
if sum(result) / len(result) == result[0]:
    print(message_for_user_2)
else:
    print(message_for_user_3)
