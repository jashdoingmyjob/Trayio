

# INPUTS:
# dimensions = array consisting of x, y pair
# start = array consisting of starting x, y dirt_loc
# dirt_loc = array of x,y tuples that describe where dirt is
# instructions = conncatenated string of driving instructions "NNWE..."

# RETURN VAL:
# JSON
def clean_up(dimensions, start, dirt_loc, instructions):
    clean_up_count = 0
    current_pos = start
    # create set of dirt_loc because better time complexity O(1) for lookups
    set_dirt_loc = set(tuple(i) for i in dirt_loc)
    for move in instructions:
        move = move.lower()
        if move == 'n' and current_pos[1] < dimensions[1]-1:
            current_pos[1] += 1
        elif move == 's' and current_pos[1] > 0:
            current_pos[1] -= 1
        elif move == 'e' and current_pos[0] < dimensions[0]-1:
            current_pos[0] += 1
        elif move == 'w' and current_pos[0] > 0:
            current_pos[0] -= 1
        # check if the current position has a dirt pile
        # by checking if the location exists in the set set_dirt_loc
        if tuple(current_pos) in set_dirt_loc:
            set_dirt_loc.remove(tuple(current_pos))
            clean_up_count += 1

    return {"final hoover position": str(current_pos[0])+" " +
            str(current_pos[1]), "patches of dirt cleaned": clean_up_count}


# INPUTS:
# file = input.txt file that contains Roomba cleaning info

# RET VAL:
# JSON
def extract_parameters_from_file(file):
    f = open(file, "r")
    param = f.readlines()
    dimen = param[0]
    start_loc = param[1]
    instructions = param[len(param)-1]
    param.remove(dimen)
    param.remove(start_loc)
    param.remove(instructions)

    if '-' in dimen:
        raise ValueError('Negative dimensions not allowed')
    dimen_list = [int(dimen[0]), int(dimen[2])]
    start_loc_list = [int(start_loc[0]), int(start_loc[2])]
    dirt_loc = param
    dirt_loc_list = []

    # append tuples so we can eventually create a set of dirt_loc
    for i in dirt_loc:
        coord = i.strip()
        dirt_loc_list.append((int(coord[0]), int(coord[2])))
    return {'dimen': dimen_list, 'start_loc': start_loc_list,
            'dirt_loc': dirt_loc_list, 'instruct': instructions}


if __name__ == "__main__":
    param_json = extract_parameters_from_file('input.txt')
    res_json = clean_up(param_json['dimen'], param_json['start_loc'],
                        param_json['dirt_loc'], param_json['instruct'])
    print(res_json['final hoover position'])
    print(res_json['patches of dirt cleaned'])
