from binary_search_tree import Binary_tree
from pickle import dump

btree = Binary_tree()

with open('anime_filtered.csv', 'r') as anime_file:
    data_line = anime_file.readline()
    anime_file.readline()
    while data_line != '':
        # print(data_line)
        start = data_line.index('"')
        end = data_line.index('"',start+1)
        genre_line = data_line[start+1:end]
        for s in genre_line.split(sep=","):
            btree.insert(s.strip().lower())
        data_line = anime_file.readline()
print(btree.get_as_array())
print(len(btree.get_as_array()))

with open('all_genres', 'bw') as stream:
    dump(btree.get_as_array(), stream)


