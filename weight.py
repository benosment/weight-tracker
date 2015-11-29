#! /usr/bin/env python3

import argparse
from datetime import datetime

weight_file = '/home/ben/Dropbox/personal/weight.csv'


def parse_args():
    # build the command line parser, setup the logger
    parser = argparse.ArgumentParser(description='logs weight, generates a graph')
    parser.add_argument('weight', action='store', help="today's weight")
    parser.add_argument('--debug', action='store_true',
                        help='display debug information')
    return parser.parse_args()


def log_weight(weight):
    ''' write todays date and weight'''
    d = '{0:%b %d %Y}'.format(datetime.now())
    with open(weight_file, 'a') as f:
        f.write('%s, %s' % (d, weight))

if __name__ == '__main__':
    args = parse_args()
    log_weight(args.weight)
    #generate_graph(weight_file)
