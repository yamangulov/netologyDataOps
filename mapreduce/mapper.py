with open('keywords_after_mapper.csv', 'w', encoding='UTF-8') as f_mapper:
    with open('keywords.csv', encoding='UTF-8') as f:
        for line in f:
            keywords_in_line = line.strip().split(',')[0].split(' ')
            for keyword in keywords_in_line:
                f_mapper.write(f'{keyword},1\n')

# after mapper.py you need to do in terminal next command for shuffle results if you are in unix-based OS:
# cat keywords_after_mapper.csv | sort > keywords_sorted.csv
# if you are in Windows you'll have problems with encoding in terminal so use shuffler.py to shuffle data

