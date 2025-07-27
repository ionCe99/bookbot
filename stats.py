import sys
def get_num_words(filepath):

    with open(filepath , 'r') as f:
        file_content = f.read()

    new_list = file_content.split()
    lenght = len(new_list)

    return lenght   

def num_of_chars(filepath):
    with open(filepath , 'r') as f:
        file_content = f.read()

    char_set = {
        'a': 0
    }
    word_list = file_content.split()
    
    for word in word_list:
        word = word.lower()
        for char in word:
            if char in char_set:
                char_set[char] +=1
            else:
                char_set[char] = 1
    sorted_dict = dict(sorted(char_set.items(),key=lambda item:item[1],reverse=True))
    for key,value in sorted_dict.items():
        print(f"{key}: {value}")
    return
