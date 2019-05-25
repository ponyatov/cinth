class Frame:
    ## implicit method for `print()` and `str()` calls
    def __repr__(self):
        return self.dump()
    
    ## static registry for already dumped elements
    ## used to avoid infinitive recursion
    dumped = []
    
    ## dump in text tree form
    def dump(self,depth=0,prefix=''):
        tree = self.pad(depth) + self.head(prefix)
        if not depth: Frame.dumped = []
        if self in Frame.dumped: return tree + ' _/'
        else: Frame.dumped.append(self)
        for j in self.nest: tree += j.dump(depth+1)
        return tree
    ## left pad with tabs
    def pad(self,n):
        return '\n' + '\t' * n
    ## header-only <T:V> form
    def head(self,prefix=''):
        return '%s<%s:%s> @%x' % (\
                prefix, self.type, self.val, id(self))
