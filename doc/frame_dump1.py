## dump in text tree form
def dump(self,depth=0,prefix=''):
    # header
    tree = self.pad(depth) + self.head(prefix)
    # avoid infinite recursion on cyclic frame graphs 
    if not depth: Frame.dumped = []
    if self in Frame.dumped: return tree + ' _/'
    else: Frame.dumped.append(self)
    # slot{}s
    for i in self.slot:
        tree += self.slot[i].dump(depth+1, i +' = ')
    # nest[]ed
    for j in self.nest:
        tree += j.dump(depth+1)
    return tree
