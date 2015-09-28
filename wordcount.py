# put your code here.

def produce_word_tokens(filename):
    """Opens text file and iterates over lines to produce word tokens.
    Returns ...
    """
    file_object = open(filename)
    tokens_list = []
    for line in file_object:
        
        punc_list = ('!', ',', '.', '--', '?', ':', ';', '"', "'", "_",
                     "(", ")")
        tokens = line.split()
        for token in tokens:
            #token = token.strip(".!?,;:")
            token_out = "".join(char for char in token if char not in punc_list)
            tokens_list.append(token_out.lower())
        # tokens_list.extend(tokens) 
        # let's ask a question about why this didn't work with extend !!!!
       
    
    # print tokens_list  # debug
    return tokens_list

def token_to_dictionary(tokens_list):
    """Convert duplicate list of words to counted dictionary of unique words.
    """
    word_dict = {}
    for token in tokens_list:
    #     if token in word_dict:
    #         word_dict[token] += 1
    #     else:
    #         word_dict[token] = 1
        word_dict[token] = word_dict.get(token, 0) + 1

    return word_dict

file_name = "twain.txt"
# file_name = "test.txt"
tokens_list = produce_word_tokens(file_name)
word_dict = token_to_dictionary(tokens_list)

# print word_dict

for key in word_dict:
    word_count = word_dict[key]
    print "{}: {}".format(key, word_count)
