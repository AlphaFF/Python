#!/usr/bin python3
# coding:utf-8

import sys,getopt
import logging

# for _ in sys.argv:
#     print(_)

def main(argv):
    input_file = ''
    output_file = ''
    test = ''
    opts,args = getopt.getopt(argv,'i:o:t:',['ifile=','ofile=','test='])
    print(opts)
    print(args)
    for opt ,arg in opts:
        print(opt)
        if opt == '-h':
            print('test.py -i <inputfile> -o <outfile>')
            sys.exit()
        elif opt in ('-i','--ifile'):
            input_file = arg
        elif opt in ('-o','--ofile'):
            output_file = arg
    print('infile:',input_file)
    print('outfile:',output_file)
    print('test:',test)

if __name__ == '__main__':
    main(sys.argv[1:])
