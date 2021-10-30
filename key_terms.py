import string


from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer


max_count = 5
news = etree.parse("news.xml")
root = news.getroot()
while len(root) < 2:
    root = root[0]
exclude_words = list(string.punctuation) + stopwords.words("english")
l_words = WordNetLemmatizer()
my_tfidf_vector = TfidfVectorizer()
freq_dict = []
dataset = []
heads = []
num_text = 0
for item in root:
    heads.append(item[0].text + ":")
    freq_dict.append({})
    tokens = [l_words.lemmatize(word) for word in word_tokenize(item[1].text.lower())]
    my_tokens = list.copy(tokens)
    for word in tokens:
        if word in exclude_words or pos_tag([word])[0][1] != "NN":
            my_tokens.remove(word)
        else:
            freq_dict[num_text].setdefault(word, 0)
            freq_dict[num_text][word] += 1
    dataset.append(" ".join(my_tokens))
    num_text += 1
tfidf_matrix = my_tfidf_vector.fit_transform(dataset)
tfidf_scores = tfidf_matrix.toarray()
all_words = my_tfidf_vector.get_feature_names_out()
# print(dataset[1])
# print(tfidf_matrix[1])
# print(tfidf_scores[1])
# print(all_words)
for ii in range(len(heads)):
    freq_words = []
    print()
    print(heads[ii])
    for word in freq_dict[ii]:
        word_index = my_tfidf_vector.vocabulary_.get(word)
        if word_index:
            freq_words.append((word, tfidf_scores[ii][word_index], freq_dict[ii][word], word_index))
            # print(word, word_index, tfidf_scores[0][word_index], freq_dict[0][word])
    freq_words.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(" ".join([w for (w, m, c, i) in freq_words[:max_count]]))
# for text in freq_dict:
#     all_words.append([])
#     for item in text:
#
#     all_words[0] = []
# all_words = my_tfidf_vector.vocabulary_

    # words = []
    # for pair in sorted(list(freq_dict.items()), key=lambda x: (x[1], x[0]), reverse=True):
    #     if len(words) < max_count:
    #         if pos_tag([pair[0]])[0][1] == "NN":
    #             words.append(pair[0])
    #     else:
    #         break
    # print(" ".join(words))
    # print()
