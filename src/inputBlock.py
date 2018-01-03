
from block import Block

class InputBlock(Block):
    tagname = None

    def __init__(self, tagname):
        super().__init__()
        self.tagname = tagname
        return None

    
