import re
import sys

def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.readlines()


def get_most_frequent_words(text):
    words = []
    for line in text:
        words += re.findall('\w+', line)

    frequency_of_words = {}

    for word in words:
        if word not in frequency_of_words:
            frequency_of_words[word] = 1
        else:
            frequency_of_words[word] += 1

        top10_frequency_of_words = sorted(frequency_of_words.items(), key=lambda x: x[1],reverse=True)[:10]
    for word in top10_frequency_of_words:
        print('Слово "%s" встречается в тексте %s раз.'% ( word[0], word[1]))


if __name__ == '__main__':
    try:
        get_most_frequent_words(load_data(sys.argv[1]))
    except IndexError as e:
        print('Вы не указали путь к файлу')
    except IOError as e:
        print('Не удалось открыть файл')
