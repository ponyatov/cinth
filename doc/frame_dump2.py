    ## static registry for already dumped elements
    ## used to avoid infinitive recursion
    dumped = []
    ## left pad with tabs
    def pad(self,n):
        return '\n' + '\t' * n
    ## header-only <T:V> form
    def head(self,prefix=''):
        return '%s<%s:%s> @%x' % (\
                prefix, self.type, self.val, id(self))
