#! /usr/bin/env python3

import argparse
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

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
        f.write('%s, %s\n' % (d, weight))


def generate_graph():
    weight_data = pd.read_csv(weight_file)
    # convert the formatted date back into a datetime object
    dates = []
    for formatted_date in weight_data['date']:
        dates.append(datetime.strptime(formatted_date, '%b %d %Y'))
    plt.plot(dates, weight_data.iloc[:, 1])
    plt.gcf().autofmt_xdate()
    plt.show()


if __name__ == '__main__':
    args = parse_args()
    log_weight(args.weight)
    generate_graph()
