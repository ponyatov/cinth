class Frame:
    ## `A // B` push B to A as a stack
    def __floordiv__(self,that):
        self.nest.append(that) ; return self
    ## `A << B` assign slot `A[B.val] = B`
    def __lshift__(self,that):
        self.slot[that.val] = that ; return self
    ## `A[key] = B` assign slot with an arbitrary name
    def __getitem__(self,key):
        return self.slot[key]
    ## `A[key]` get frame from given slot
    def __setitem__(self,key,that):
        self.slot[key] = that ; return self
