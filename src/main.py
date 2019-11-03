from __future__ import division
import sys

import extract_frequent_pattern


def calculate_nodes_in_projection(patterns, ch_dict=None):
    if ch_dict is None:
        raise ValueError
    nodes_in_proj = set()

    for item in patterns:
        path = set(ch_dict[item])
        # print  [node.value for node in path]
        nodes_in_proj = nodes_in_proj | path
    return len(nodes_in_proj)


def calculate_drank(patterns, ch_dict=None, ch_height=None):
    if ch_dict is None or ch_height is None:
        raise ValueError

    num_node_in_proj = calculate_nodes_in_projection(patterns, ch_dict=ch_dict)
    num_item_in_pat = len(pattern)
    h = ch_height

    try:
        drank = (num_node_in_proj - (num_item_in_pat + h - 1)) / (
            (h-1)*(num_item_in_pat -1))
    except ZeroDivisionError as e:
        drank = "NOT PROCESSED"

    return drank


def read_input():
    if len(sys.argv) < 3:
        print("program expects name of input file and pattern file")
        sys.exit(1)

    try:
        in_filname = sys.argv[1]
        pat_filename = sys.argv[2]
        fin = open(in_filname, 'r')
        fpat = open(pat_filename, 'r')
    except:
        print("file not found")
        sys.exit(1)

    item_path_dict = {}
    is_item = True
    cur_item = ''
    path = []
    for line in fin.readlines():
        path = []
        if line.strip() == '':
            continue

        if is_item:
            # line is item
            item = line.strip()
            cur_item = item
            is_item = 0
        else:
            # line is path
            path = line.strip().split(' ')
            item_path_dict[cur_item] = path
            is_item = 1
    
    # threshold randomly decided
    freq_patterns =extract_frequent_pattern.extract_frequent_patterns(fpat, 18)
    
    return (item_path_dict, freq_patterns)

def main():
    (item_path_dict, freq_patterns) = read_input()
    ch_height = 0
    for item in item_path_dict.keys():
        if len(item_path_dict[item]) > ch_height:
            ch_height = len(item_path_dict[item])

    print("concept hierarchy height")
    print (ch_height)
    dranks = [0]*len(freq_patterns)
    idx = 0
    for patterns in freq_patterns:
        print("processing pattern %s", ' '.join(patterns), '\n')
        try:
            # calculate drank
            dranks[idx] = calculate_drank(patterns, ch_dict=item_path_dict, ch_height=ch_height)
        except KeyboardInterrupt:
            dranks[idx] = "SKIPPED"

        print(str(dranks[idx]), '\n')
        idx += 1

    # convert patterns to list
    fin_patterns = []
    for i in freq_patterns:
        fin_patterns.append(' '.join(i))

    # Now we have drank for evey frequent pattern.
    for i in range(0, len(freq_patterns)):
        print("patterns ", str(i), "- ",)
        print(fin_patterns[i])
        print("drank - ")
        print(dranks[i])
        print('\n')

if __name__ == '__main__':
    main()