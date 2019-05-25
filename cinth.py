from FixTk import prefix

class Frame:
    def __init__(self,V):
        self.type = self.__class__.__name__.lower()
        self.val  = V
        self.slot = {}
        self.nest = []
        
    def __repr__(self):
        return self.dump()
    def dump(self,depth=0,prefix=''):
        tree = self.pad(depth) + self.head(prefix)
        if not depth: Frame.dumped = []
        if self in Frame.dumped: return tree + ' _/'
        else: Frame.dumped.append(self)
        for j in self.nest: tree += j.dump(depth+1)
        return tree
    def pad(self,n):
        return '\n' + '\t' * n
    def head(self,prefix=''):
        return '%s<%s:%s> @%x' % (prefix, self.type, self.val, id(self))
                                    
    def __floordiv__(self,that):
        self.nest.append(that) ; return self
        
class Active(Frame): pass

class Cmd(Active): pass

class VM(Active): pass

class IO(Frame): pass

class Dir(IO): pass

class File(IO): pass

class Meta(Frame): pass

class Project(Meta): pass

prj = Project('ide')

home = Dir('~') ; prj // home

settings = Dir('.settings') ; home // settings

print prj
