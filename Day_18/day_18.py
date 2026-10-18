import re
from collections import Counter

paragraph = """I love teaching. If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the
capabilities to develop an application what else can you love."""

def most_frequent_words(text, n=10):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    word_counts = Counter(words)
    return [(count, word) for word, count in word_counts.most_common(n)]

print(most_frequent_words(paragraph))


import keyword

def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)


print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))


import re
from collections import Counter

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;.
There $is nothing; &as& mo@re rewarding as educa@ting &and&
@emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting
tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a
tea@cher!?'''


def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def most_frequent_words(text):
    words = text.split()
    word_counts = Counter(words)
    return [(count, word) for word, count in word_counts.most_common(3)]


cleaned_text = clean_text(sentence)

print(cleaned_text)
print(most_frequent_words(cleaned_text))