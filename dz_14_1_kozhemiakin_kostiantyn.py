class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    def add_elements(self, list_of_node):
        for node in list_of_node:
            self.insert(node)

    def find_min(self):
        if self.left:
            self.left.find_min()
        if not self.left:
            return str(self.id_node)

    def find_max(self):
        if self.right:
            self.right.find_max()
        return self

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()


tr = Tree(5)
my_list = [5, 65, 3, 1, 5777, 56, 35, 90]
tr.add_elements(my_list)
# # tr.print_tree()
# tr.insert(80)
# # tr.print_tree()
# tr.insert(80)
# # tr.print_tree()
# tr.insert(80)
# tr.print_tree()
# tr.findval(1)
print(tr.find_min())
