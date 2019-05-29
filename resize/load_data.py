import json
import os
import sys
from collections import OrderedDict

class LoadData:
    def __init__(self):
        ## Get directory for file path
        self.file_dir = os.path.dirname(__file__)
        self.head, self.tail = os.path.split(self.file_dir)
        if(self.tail != 'Gen-Desc.docx'): 
          self.file_dir = self.head
        pass

    def getFile(self, file_path):
        return os.path.join(self.file_dir, file_path)

    def getInputFilePath(self):
        # if called with no arguments, call app data pick file from there
        path = None
        if (len(sys.argv) > 1):
            path = self.getFile(sys.argv[1])
            
        else:
            path = self.getFile(os.getenv('LOCALAPPDATA') + "\\Trevexs SSC\\data\\sample1.trsc")
        
        return path

    def getInputValues(self):
        self.path = self.getInputFilePath()
        return json.load(open(self.getFile(self.path), encoding='utf8'), 
            object_pairs_hook=OrderedDict)