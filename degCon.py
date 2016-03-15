"""degCon.
CNU UAS Team's degree conversion software

Usage:
  degCon.py
  degCon.py <d> [<m>] [<s>] [--out <file>]
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

SUPPORTED_FILETYPE = [".txt", ".csv"]

def main(arguments):
    """Main Function
    Args:
      arguments (dictionary): The parameters dictionary. See above

    Returns:

    """
    print "entered main"

    d = arguments['<d>']
    m = arguments['<m>']
    s = arguments['<s>']

    df = float(d)

    toDD = False
    if(m != None and s != None):
        mf = float(m)
        sf = float(s)
        toDD = True
        
    if(toDD == False and df.is_integer()):
        print 'Convert {0} to D,M,S. Are you Sure (Y/n)?'.format(df)
        if(raw_input().lower() == 'n'):
            print 'exiting'
            exit(1)

    if(toDD == False):
        from_dd(df)
    else:
        from_dms(df,mf,sf)

def from_dd(dd):
    print 'entered from_dd', dd
    d = int(dd)
    m = int((dd - d) * 60)
    s = int((dd - d - m/60) * 3600)
    print 'out: ', d, ',', m, ',', s
    output.write(str(d) + ',' + str(m) + ',' + str(s))

def from_dms(d, m, s):
    print 'entered from_dms', d, m, s
    dd = d + m/60 + s/3600
    print 'out: ', dd
    output.write(str(dd))

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
