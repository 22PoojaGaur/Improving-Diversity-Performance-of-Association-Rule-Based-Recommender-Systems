# @author 22PoojaGaur


from __future__ import division
import sys
import copy

import extract_frequent_pattern

class Node(object):
    """A node in a tree"""
    def __init__(self, id, value, children=[], is_dummy=False, depth=0):
        super(Node, self).__init__()
        self.id = id
        self.value = value
        self.children = copy.deepcopy(children)
        self.depth = depth
        self.is_dummy = is_dummy

    def is_leaf(self):
        return len(self.children) == 0


class Tree(object):
    """Tree class to with multiple children for each node"""
    def __init__(self):
        super(Tree, self).__init__()
        self.root = None
        self.node_count = 0
        self.height = 0
        self.nodes_at_level = {}
        self.real_edges_at_level = {}
        self.fake_edges_at_level = {}
        
    def insert_nodes(self, nodes):
        """
        Make sure that all given nodes are in tree, if not
        creates them.
        """

        # if root empty insert root
        if self.root == None:
            self.height += 1
            self.node_count += 1
            self.root = Node(self.node_count, nodes[0], depth=1)

        # insert rest
        current = self.root
        for node in nodes[1:]:
            child_vals = [c.value for c in current.children]
            if node not in child_vals:
                if self.height < current.depth+1:
                    self.height = current.depth+1
                self.node_count += 1
                current.children.append(Node(self.node_count, node, depth=(current.depth+1)))

            child_vals = [c.value for c in current.children]
            
            for cnum in range(0, len(current.children)):
                if current.children[cnum].value == node:
                    current = current.children[cnum]
                    break

        return

    def print_tree(self):
        """Prints tree in level order."""

        if self.root is None:
            print("Tree is not built")
            return

        print(self.root.value + '\n')
        queue = [self.root]
        while len(queue) > 0:
            current = queue[0]

            has_child = 0
            
            for child in current.children:
                print(child.value + " - ",)
                queue.append(child)
                has_child = 1

                if child.is_leaf():
                    print("leaf node depth ", child.depth)
            if has_child:
                print('\n')
                has_child = 0
            if len(queue) >= 1:
                queue = queue[1:]

        return

    def find_path_to_node(self, current, item, current_path):
        # print "current node "
        # print current.value
        # print "current_path "
        # print [cur.value for cur in current_path]
        cur_p = copy.deepcopy(current_path)
        cur_p.append(current)
        current_path = cur_p

        if current.value == item:
            return current_path

        for child in current.children:
            path = self.find_path_to_node(child, item, current_path)
            if path is not None:
                return path

    def calculate_nodes_in_projection(self, pattern):
        nodes_in_proj = set()

        for item in pattern:
            #print item
            path = self.find_path_to_node(self.root, item, [])
            #print  [node.value for node in path]
            for node in path:
                nodes_in_proj.add(node)

        # print [node.value for node in nodes_in_proj]
        return len(nodes_in_proj)

    def calculate_drank(self, pattern):
        num_node_in_proj = self.calculate_nodes_in_projection(pattern)
        num_item_in_pat = len(pattern)
        h = self.height

        try:
            # print "number of nodes in projection "
            # print num_node_in_proj
            # print "number of item in pattern "
            # print num_item_in_pat
            # print "height of tree "
            # print h
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
    freq_patterns =extract_frequent_pattern.extract_frequent_patterns(fpat, 500)
    
    return (item_path_dict, freq_patterns)

def main():
    (item_path_dict, freq_patterns) = read_input()

    # building concept hierarchy for all patterns
    CH = Tree()
    for item in item_path_dict.keys():
        CH.insert_nodes(item_path_dict[item])
    CH.print_tree()
    dranks = [0]*len(freq_patterns)
    idx = 0
    for pattern in freq_patterns:
        print("processing pattern %s", ' '.join(pattern), '\n')
        try:
            dranks[idx] = CH.calculate_drank(pattern)
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
        print("pattern ", str(i), "- ",)
        print(fin_patterns[i])
        print("drank - ")
        print(dranks[i])
        print('\n')

if __name__ == '__main__':
    main()
