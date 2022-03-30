previous_word = None
word_count = 0
with open('result.csv', 'w', encoding='UTF-8') as f_writer:
    with open('keywords_sorted.csv', encoding='UTF-8') as f:
        for i, line in enumerate(f):
            if i != 0:
                keyword, one = line.strip().split(',')
                one = int(one)
                if previous_word:
                    if previous_word == keyword:
                        word_count += one
                    else:
                        f_writer.write(f'{previous_word},{word_count}\n')
                        word_count = one
                        previous_word = keyword
                else:
                    previous_word = keyword
                    word_count = one
    f_writer.write(f'{previous_word},{word_count}\n')

