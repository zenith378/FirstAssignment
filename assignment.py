import argparse, os
import time
start_time = time.time()



def dir_path(filepath):
    if os.path.isdir(filepath):
        return filepath
    else:
        raise NotADirectoryError(filepath)

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=dir_path)











print("--- %s seconds ---" % (time.time() - start_time))