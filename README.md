# Degree-Converter
Python script for converting between decimal degrees and degree, minute, seconds

CNU UAS Team's degree conversion software

Usage:
  degCon.py <d> [<m> <s>]
  degCon.py --import <file> [--out <file>]
  degCon.py -h | --help
  degCon.py --version
  
Options:
  -h, --help                    show this screen.
  -i <file>, --import <file>    convert degrees from a file.
  -o <file>, --out <file>       where to output the results [default: output.txt]
  
  
dependencies: docopt, Python 2.7.*

to setup docopt:
  pip install docopt
  
just run degCon.py with command line arguments
