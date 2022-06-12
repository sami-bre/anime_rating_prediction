import pickle

mov_map = dict()

with open('anime_filtered.csv', 'r') as anime_filtered_file:
    with open('mov_map', 'wb') as mov_map_file:
        line = anime_filtered_file.readline()
        while line != '':
            first_comma_index = line.index(',')
            mov_id = line[:first_comma_index]
            start = line.index('"')
            end = line.index('"',start+1)
            genre_line = line[start+1:end]
            mov_map[mov_id] = [genre.strip().lower() for genre in genre_line.split(',')]
            line = anime_filtered_file.readline()
        pickle.dump(obj=mov_map, file=mov_map_file)

    