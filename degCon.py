"""degCon.
CNU UAS Team's degree conversion software

Usage:
  degCon.py
  degCon.py <d> [<m> <s>]
  degCon.py [--import <file>] [--out <file>]
  degCon.py -h | --help
  degCon.py --version
  
Options:
  -h, --help                    show this screen.
  -i <file>, --import <file>    convert degrees from a file.
  -o <file>, --out <file>       where to output the results [default: output.txt]

"""
# The above docstring is used for arguments
### DO NOT MONDIFY ABOVE THIS COMMENT ####

__author__ = 'Christopher Newport Unmanned Aerial Systems Lab Software Team'

# Import from libs folder
# Docopt is used for parsing command line args.
from docopt import docopt
import os

SUPPORTED_FILETYPE = [".txt", ".csv"]

def main(args):
    """Main Function
    Args:
      arguments (dictionary): The parameters dictionary. See above

    Returns:

    """

    inFile = False
    degrees = []
    
    if(args['--import'] != None):
        inFile = True
        with open(args['--import'], "r") as inStream:
            for line in inStream:
                currLine = line.rstrip('\n').split(",")
                degrees.append(currLine)
    else:
        line = []
        line.append(args['<d>'])
        line.append(args['<m>'])
        line.append(args['<s>'])
        degrees.append(line)
                    
    print degrees

    for deg in degrees:
        df = float(deg[0])

        toDD = False
        if(len(deg) == 3 and deg[1] != None and deg[2] != None):
            mf = float(deg[1])
            sf = float(deg[2])
            toDD = True
            
        if(toDD == False and df.is_integer()):
            print 'Convert {0} to D,M,S. Are you Sure (Y/n)?'.format(df)
            if(raw_input().lower() == 'n'):
                print 'exiting'
                exit(1)

        if(toDD == False):
            cnvtd = from_dd(df)
        else:
            cnvtd = from_dms(df,mf,sf)
        out_str = ", ".join(str(i) for i in cnvtd)
        output.write(out_str)
        print out_str


def from_dd(dd):
    print 'entered from_dd', dd
    cnvtd = []
    cnvtd.append(int(dd))
    cnvtd.append(int((dd - cnvtd[0]) * 60))
    cnvtd.append(int((dd - cnvtd[0] - cnvtd[1]/60) * 3600))
    return cnvtd

def from_dms(d, m, s):
    cnvtd = []
    print 'entered from_dms', d, m, s
    cnvtd.append(d + m/60 + s/3600)
    return cnvtd

    ## TODO: add other argument functionality in here

if __name__ == '__main__':
    # Parse args
    arguments = docopt(__doc__, version="0.1.0")
    print arguments
    
    # setup output file
    output_file = arguments['--out']
    output = open(output_file, "wb")
    
    main(arguments)
    
    output.close()
