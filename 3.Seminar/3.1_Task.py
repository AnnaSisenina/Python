list_dict = [{"V": "S001"}, {"V": "S002"},
             {"VI": "S001"}, {"VI": "S005"},
             {"VII": " S005 "}, {"V": " S009 "},
             {"VIII": " S007 "}]


n_list = []
for i in list_dict:
    w_list = list(i.values())
    word = w_list[0]
    word_clear = word.strip()
    n_list.append(word_clear)

print(set(n_list))