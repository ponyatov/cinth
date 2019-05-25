class Frame:
    ## implicit method for `print()` and `str()` calls
    def __repr__(self):
        return self.dump()
