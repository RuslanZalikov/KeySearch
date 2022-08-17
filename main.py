import function

def keywordsearch(name_file):
    threshold_word = 0.8
    threshold_combination = 200
    threshold_combination_lap = 10

    with open("NO_TOUCH/KEYWORD") as file:
        KEYWORD = function.KeyWord(file.read())
    with open("NO_TOUCH/KEYWORD_LAP") as file:
        KEYWORD_LAP = function.KeyWord(file.read())
    with open(f"input_file/{name_file}") as file:
        INPUT = function.KeyWord(file.read())

    for index, value in enumerate(KEYWORD.text):
        KEYWORD.text[index] = function.Word(value, index)

    for index, value in enumerate(KEYWORD_LAP.text):
        KEYWORD_LAP.text[index] = function.Word(value, index)

    for index, value in enumerate(INPUT.text):
        INPUT.text[index] = function.Word(value, index)

    INPUT_2 = INPUT

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
        print(value)

    for index, value in enumerate(INPUT_2.text):
        for second in KEYWORD_LAP.text:
            INPUT_2.text[index].rate = max(function.comporation(value.word, second.word), INPUT_2.text[index].rate)
    passed_the_test_lap = []
    for index, value in enumerate(INPUT_2.text):
        if value.rate >= threshold_word:
            passed_the_test_lap.append(value)
            # print(f"{value}:{value.index}:{value.rate}")
    pair_passed_lap = []
    for index in range(len(passed_the_test_lap)-1):
        for jndex in range(index + 1, len(passed_the_test_lap)):
            pair_passed_lap.append((2 - passed_the_test_lap[index].rate)*(2 - passed_the_test_lap[jndex].rate)*((abs(passed_the_test_lap[jndex].index - passed_the_test_lap[index].index))**2))
    # print(pair_passed)

    for value in pair_passed_lap:
        print(value)

    value_min = 1e9
    value_min_lap = 1e9
    for value in pair_passed:
        if value < value_min:
            value_min = value
    for value in pair_passed_lap:
        if value < value_min_lap:
            value_min_lap = value
    if value_min_lap <= threshold_combination_lap:
        return "LAP"
    elif value_min <= threshold_combination:
        return "LAU"
    return 0
print(keywordsearch('INPUT'))
