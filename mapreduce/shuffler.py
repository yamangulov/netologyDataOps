keywords = []

with open('keywords_after_mapper.csv', encoding='UTF-8') as f:
    for line in f:
        keywords.append(line)

with open('keywords_sorted.csv', 'w', encoding='UTF-8') as f_writer:
        keywords.sort()
        for keyword in keywords:
            f_writer.write(keyword)
