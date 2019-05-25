class Frame:
    ## construct frame with given name `V`
    def __init__(self,V):
        # type/class tag
        # (represented as a string for simplicity)
        self.type = self.__class__.__name__.lower()
        # scalar value (implementation language type)
        self.val  = V
        # named slots = attributes = associative array 
        self.slot = {}
        # nested elements = vector = stack = (de)queue
        self.nest = []
