#!/usr/bin/env python
""" Take a list of cards and reduce them to a list of all sets containing those cards
"""

import argparse
import json
import logging
import collections
import re
import yaml
import mtgsdk

LOGGER = logging.getLogger(__name__)



def parse_list(path):
    """ Take path from the command line and try to parse the file into a list of cards
    """
    with open(path) as contents:
        text = contents.read()
        try:
            cards = json.loads(text)
            return cards
        except json.decoder.JSONDecodeError:
            LOGGER.debug('Nope, not valid json. Try yaml.')
        try:
            cards = yaml.load(text, Loader=yaml.FullLoader)
            assert isinstance(cards, list)
            return cards
        except AssertionError:
            LOGGER.debug('Not a yaml list either. Try text.')
        cards = text.strip().split('\n')
        return cards

def run(args):
    """ Take the list of cards, look them up, and reverse into a dict of set:cards
    """
    LOGGER.info('Got me a list of cards, here: %s', args.list)
    sets = collections.defaultdict(list)
    search = mtgsdk.Card.where(name='|'.join(args.list)).all()
    for item in search:
        if args.exact_name and item.name not in args.list:
            continue
        if args.filter_sets and any([re.search(pattern, item.set_name) for pattern in args.filter_sets]):
            continue
        sets[item.set_name].append(item.name)
    LOGGER.warning('Cards per set:\n%s', yaml.safe_dump(dict(sets), default_flow_style=False))


def main():
    """ Main entry
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('list',
                        help=('Path to a file containing a list of cards. May be yaml, json, or newline-delimited'
                              ' text.'),
                        type=parse_list)
    parser.add_argument("-e", '--exact-name',
                        dest='exact_name',
                        help="Search card names exactly",
                        action='store_true',
                        default=False)
    parser.add_argument("-f", '--filter-sets',
                        dest='filter_sets',
                        help="Filter out set names matching pattern. May be set multiple times.",
                        action='append')
    parser.add_argument("-v", '--verbose',
                        help="Verbose",
                        action='count',
                        default=0)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    levels = [logging.WARN, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels)-1, args.verbose)]
    LOGGER.setLevel(level)
    LOGGER.addHandler(logging.StreamHandler())
    args.func(args)

if __name__ == '__main__':
    main()
