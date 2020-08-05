#!/usr/bin/env python3 

import sys
import os
import pandas as pd

def get_size(path):
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total += get_size(entry.path)
            total += entry.stat(follow_symlinks=False).st_size
        except Exception as e:
            print('Exception: ',e)
            total += 0
    return total


def main():
    path = '/home'
    print("total arguments passed: ", len(sys.argv))
    
    directory = sys.argv[1] if len(sys.argv) >= 2 else path
    
    paths = []
    usage =[]

    for entry in os.scandir(directory):
        #print(entry)
        if (entry.is_dir(follow_symlinks=False)):
            # print(entry.path + ' issa dir')
            # print(get_size(entry.path))
            total = get_size(entry.path)
            usage.append(total)
            paths.append(entry.path)
        
        usage_dict = {'directory': paths, 
                        'usage': usage}
    df = pd.DataFrame(usage_dict)
    print(df)
    df.to_csv('disk_home_usage.csv')

if __name__ == '__main__':
    main()
    
