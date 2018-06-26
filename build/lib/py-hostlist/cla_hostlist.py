import argparse
import sys
import hostlist as hl 

"""
Command-line arguments for hostlist.py 

Author: Christopher Moussa (moussa1@llnl.gov)
Mentor: Elsa Gonsiorowski (gonsiorowski1@llnl.gov)
Date: June 26, 2018
"""


def msg(name=None):
	return '''
	Description: cla_hostlist processes slurm-style hostlist strings and 
	can return those strings in manipulated fashion. 
	
	Usage: python cla_hostlist.py [OPTION]... [HOSTLIST]...

  	-h, --help                   Display this message.
  	-e, --expand                 Expand a compressed hostlist
  	-a, --abbreviate             Compress an expanded hostlist
  	-t, --tighten                Return a hostlist string
  	-m, --minus                  Subtract all HOSTLIST args from first HOSTLIST
  	-i, --intersection           Intersection of all HOSTLIST args
  	-u, --union                  Union of all HOSTLIST arguments
  	-n, --nth=N                  Output the host at index N
  	-S, --sort                   Return sorted HOSTLIST 
  	-c, --count                  Print the number of hosts
  	-F, --find=HOST              Output position of HOST in result HOSTLIST
		'''

parser = argparse.ArgumentParser(usage=msg())

parser.add_argument("-e", "--expand", dest="expand")

parser.add_argument("-a", "--abbreviate", dest="compress_range")

parser.add_argument("-t", "--tighten", dest="compress")

parser.add_argument("-m", "--minus", dest="diff", nargs="*")

parser.add_argument("-i", "--intersection", dest="intersection", nargs="*")

parser.add_argument("-u", "--union", dest="union", nargs="*")

parser.add_argument("-n", "--nth=N", dest="nth", nargs="*")

parser.add_argument("-s", "--sort", dest="sort")

parser.add_argument("-c", "--count", dest="count")

parser.add_argument("-f", "--find", dest="find", nargs="*")

args = parser.parse_args()

if args.expand:
	hl.expand(args.expand)
if args.compress_range:
	hl.compress_range(args.compress_range)
if args.compress:
	hl.compress(args.compress)
if args.diff:
	hl.diff(args.diff[0], args.diff[1])
if args.intersection:
	hl.intersect(args.intersection[0], args.intersection[1])
if args.union:
	hl.union_nodes(args.union[0], args.union[1])
if args.nth:
	hl.nth(args.nth[0], args.nth[1])
if args.sort:
	hl.sort_nodes(args.sort)
if args.count:
	hl.count(args.count)
if args.find:
	hl.find(args.find[0], args.find[1])