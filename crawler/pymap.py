#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import logging

from crawler import build_site_map

logger = logging.getLogger('SiteMap Builder')


@click.command()
@click.argument('url')
@click.option('--debug', 'debug', flag_value=True, default=False, help='Run in Debug Mode.')
def _build_site_map(url, debug):
    if debug:
        logger.setLevel(logging.DEBUG)
    print build_site_map(url)

if __name__ == '__main__':
    _build_site_map()
