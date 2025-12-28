def get_num_words(text):
	words = text.split()
	return len(words)

def get_string(text):
	string_dict = {}

	for chr in text:
		ch = chr.lower()
		if ch in string_dict:
			string_dict[ch] = string_dict[ch] + 1
		else:
			string_dict[ch] = 1

	return string_dict

def sort_on(one_dict):
	return one_dict["num"]

def sort_on(one_dict):
    return one_dict["num"]


def sort_chars(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        char_dict = {
            "char": char,
            "num": count,
        }
        sorted_list.append(char_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
