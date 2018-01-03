import os
import time

from block import Block

class OutputBlock(Block):
    def __init__(self):
        super().__init__()
        return

    def recv_tag_point(self, tag_point):
        super().recv_tag_point(tag_point)
        # save to local backup
        self.save_to_csv(self.local_backup_filepath(tag_point), tag_point)
        return

    def save_to_csv(self, csv_path, tag_point):
        csv_file = open(csv_path,'a+')
        csv_file.write(tag_point.tagname + ','
                       + time.strftime('%Y/%m/%d %H:%M:%S',tag_point.timestamp) + ','
                       + str(tag_point.value) + '\n')
        csv_file.close()
        return

    def get_last_tag_point(self, tag_point):
        if (tag_point.type == str):
            tag_point = TagPoint(tag_point,"","")
        csv_file = None
        try:
            with open(self.local_backup_filepath(tag_point)) as f:
                f.seek(-2, os.SEEK_END)
                while (f.read(1) != b"\n"):
                    f.seek(-2,os.SEEK_CUR)
                last = f.readline()
                split = last.split(',')
                print(split[-1])
        except Exception:
            return 0
        
