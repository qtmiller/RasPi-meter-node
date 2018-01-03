import copy

from processBlock import ProcessBlock
from tagPoint import TagPoint

class Accumulator(ProcessBlock):

    def __init__(self):
        super().__init__()
        return None

    def recv_tag_point(self, tag_point):
        if len(self.recent_tag_points) == 0:
            self.recent_tag_points.append( \
                super().get_last_tag_point(copy.copy(tag_point)))
        accu_tag_point = copy.copy(tag_point)
        accu_tag_point.value = (self.recent_tag_points[-1].value +
                                    tag_point.value)
        super().recv_tag_point(accu_tag_point)
        self.send_tag_point()
        
