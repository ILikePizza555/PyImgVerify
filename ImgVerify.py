'''
Created on Jul 18, 2013

@author: isaac
'''
import os
import sys
import getopt
from PIL import Image

'''
Class for containing color escape codes
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def testImage(path):
    try:
        i = Image.open(path)
        return i.format == 'JPEG' or i.format == 'BMP' or i.format == 'PNG' or i.format == 'GIF'
    except IOError:
        return False;

def getFileList(path, verbose = False):
    #Bad Images!
    bdimg_lst = []
      
    for root, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                #File seems to be an image
                
                if verbose == True:
                    #Only print colors if verbose is enabled
                    print bcolors.OKBLUE + "Found file at " + os.path.join(root, file) + bcolors.ENDC
                
                #Test the image
                if testImage(os.path.join(root, file)) == False:
                    #Not an Image
                    print bcolors.FAIL + "File at " + os.path.join(root, file) + " isn't an image!" + bcolors.ENDC
                    bdimg_lst.append(os.path.join(root, file))
                    
            else: 
                if verbose == True:
                    #Verbose Enabled, print all of the files we walk through
                    print os.path.join(root, file)

def main(argv):
    path = None
    verbose = False
    
    try:
        opts, args = getopt.getopt(argv, "p:v", ["path=", "verbose"])
    except getopt.GetoptError:
        print opts, args
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-p, --path"):
            path = arg
        elif opt in ("-v, --verbose"):
            verbose = True
            
    if path != None:
        getFileList(path, verbose)
    else:
        print bcolors.FAIL + "No path specified!" + bcolors.ENDC

if __name__ == '__main__':
    main(sys.argv[1:])
        
        