import math

# Function for tokenizing documents 
def create_bows(docs):
    bows = []
    for doc in docs:
        bows.append(doc.split(' '))
    return bows

# Function for taking any number on documents/ Bag Of Words and return the word list 
def collect_docs(bows):
    bows_list = []
    for bow in bows:
        bows_list = set(bows_list).union(set(bow))
    return bows_list

# Function for creating dictionary for every document and put them in a list
def create_dicts(bows_num, word_set):
    dict_list = []
    for i in range(bows_num):
        dict_list.append(dict.fromkeys(word_set, 0))
    return dict_list

# Function for counting how often a word in document
def count(bow, dict):
    for word in bow:
        dict[word] += 1

# Function for computing Term Frequency
def TF(doc, bow):
    tf = {}
    bow_count = float(len(bow))
    for word, count in doc.items():
        tf[word] = count / bow_count
    return tf

# Function for computing the IDF
def IDF(word_set, docs):
    idf = {}
    N = len(docs)
    idf_dict = dict.fromkeys(word_set, 0)

    for doc in docs:
        for word, val in doc.items():
            if val > 0:
                idf_dict[word] += 1

    for word, val in idf_dict.items():
        idf[word] = math.log10(N / float(val))

    return idf

# To give the final TF-IDF score
def compute_score(tf, idf):
    scores = {}
    for word, val in tf.items():
        scores[word] = val * idf[word]
    return scores


def compute_TF_IDF(*docs):
    bows = create_bows(docs)
    # print(bows)

    word_set = collect_docs(bows)
    # print(word_set)

    docs_dicts = create_dicts(len(docs), word_set)
    # print(docs_dicts[0])

    i = 0
    tf_list = []
    for bow in bows:
        count(bow, docs_dicts[i])
        tf_list.append(TF(docs_dicts[i], bow))
        i += 1
    # print(tf_list)

    idf = IDF(word_set, docs_dicts)
    # print(idf)

    scores = []
    for tf in tf_list:
        scores.append(compute_score(tf, idf))
    return scores


def main():
    # documents to work on
    S1 = "The car is driven on the road"; S2 = "The truck is driven on the highway"; S3 = "The buses are driven on the street"

    scores = compute_TF_IDF(S1, S2, S3)
    
    for score in scores:
        print(score)
    

main()


