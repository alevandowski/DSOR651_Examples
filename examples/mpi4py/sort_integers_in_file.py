

def sort_integers_in_file(file_path):
    with open(file_path, "r") as f:
        # first sort integers in file as they are read
        sorted_integers = []
        n = 0
        for line in f:
            integer = int(line)
            index_to_insert = n
            # TODO: since the integers are sorted, could use binary search to optimize the following code
            for i, v in enumerate(sorted_integers):
                if integer < v:
                    index_to_insert = i
                    break
            n = n + 1
            sorted_integers.insert(index_to_insert, integer)
    return sorted_integers
