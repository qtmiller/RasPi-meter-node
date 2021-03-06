import os

from outputBlock import OutputBlock

class FtpLocalSave(OutputBlock):

    def __init__(self):
        super().__init__()
        return

    def recv_tag_point(self, tag_point):
        super().recv_tag_point(tag_point)
        super().save_to_csv(self.local_ftp_filepath(tag_point), tag_point)
        return

    def local_ftp_filepath(self, tag_point):
        script_dir = os.path.dirname(os.path.realpath('__file__'))
        parent_dir = script_dir.rstrip('/src')
        tag_path = 'ftp/' + tag_point.tagname
        filepath = os.path.join(parent_dir, tag_path, 'records.csv')
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        return filepath
