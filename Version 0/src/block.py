import os

class Block(object):
    
    def __init__(self):
        self.recent_tag_points = []
        self.input_blocks = []
        self.output_blocks = []
        self.recent_tp_limit = 10
        return
    
    def send_tag_point(self):
        # check for point
        if not len(self.recent_tag_points) == 0:
            # send to all outputs
            for out in self.output_blocks:
                out.recv_tag_point(self.recent_tag_points[-1])
        return None

    def recv_tag_point(self, tag_point):
        self.recent_tag_points.append(tag_point)
        while len(self.recent_tag_points) > self.recent_tp_limit:
            self.recent_tag_points.remove(self.recent_tag_points[1])
        return None

    def get_last_tag_point(self):
        return self.recent_tag_points[-1]

    def set_last_tag_point(self, tag_point):
        self.recent_tag_points.append(tag_point)
        return None

    def get_param_dict(self):
        param_dict = {}
        param_dict['recent_tp_limit'] = self.recent_tp_limit
        return None

    def set_param_dict(self, param_dict):
        if (param_dict['recent_tp_limit'] != None):
            recent_tp_limit = param_dict['recent_tp_limit']

    def connect_input(self, block_object):
        # remove input if already connected
        self.disconnect_input(block_object)
        # add input to list
        self.input_blocks.append(block_object)
        return None

    def disconnect_input(self, block_object):
        # remove block from input list if present
        try:
            self.input_blocks.remove(block_object)
        except Exception:
            pass
        return None

    def connect_output(self, block_object):
        # remove output if already connected
        self.disconnect_output(block_object)
        # add output to list
        self.output_blocks.append(block_object)
        # add self to block_object input list
        block_object.connect_input(self)
        return None

    def disconnect_output(self, block_object):
        # remove self from block_object input list
        block_object.disconnect_input(self)
        # remove block from output list if present
        try:
            self.output_blocks.remove(block_object)
        except Exception:
            pass
        return None

    def local_backup_filepath(self, tag_point):
        script_dir = os.path.dirname(os.path.realpath('__file__'))
        parent_dir = script_dir.rstrip('/src')
        tag_path = 'tags/' + tag_point.tagname
        filepath = os.path.join(parent_dir, tag_path, 'records.csv')
        return filepath
