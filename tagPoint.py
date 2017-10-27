
class TagPoint(object):
    tagname = None
    timestamp = None
    value = None

    def __init__(self, tagname, timestamp, value):
        self.tagname = tagname
        self.timestamp = timestamp
        self.value = value
        return

    def setValue(self, new_value):
        self.value = new_value
        return
