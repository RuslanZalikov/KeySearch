import function

def keywordsearch(name_file):
    threshold_word = 0.8
    threshold_combination = 200

    with open("NO_TOUCH/KEYWORD") as file:
        KEYWORD = function.KeyWord(file.read())
    with open(f"input_file/{name_file}") as file:
        INPUT = function.KeyWord(file.read())

    for index, value in enumerate(KEYWORD.text):
        KEYWORD.text[index] = function.Word(value, index)

    for index, value in enumerate(INPUT.text):
        INPUT.text[index] = function.Word(value, index)

    for index, value in enumerate(INPUT.text):
        for second in KEYWORD.text:
            INPUT.text[index].rate = max(function.comporation(value.word, second.word), INPUT.text[index].rate)
    passed_the_test = []
    for index, value in enumerate(INPUT.text):
        if value.rate >= threshold_word:
            passed_the_test.append(value)
            # print(f"{value}:{value.index}:{value.rate}")
    pair_passed = []
    for index in range(len(passed_the_test)-1):
        for jndex in range(index + 1, len(passed_the_test)):
            pair_passed.append((2 - passed_the_test[index].rate)*(2 - passed_the_test[jndex].rate)*((abs(passed_the_test[jndex].index - passed_the_test[index].index))**2))
    # print(pair_passed)
    for value in pair_passed:
        if value <= threshold_combination:
            return 1
    return 0
print(keywordsearch('INPUT'))
