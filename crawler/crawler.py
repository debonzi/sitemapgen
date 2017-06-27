# -*- coding: utf-8 -*-

import logging
import lxml.html

import requests

from jinja2 import Environment, PackageLoader, select_autoescape

logging.basicConfig()
logger = logging.getLogger('SiteMap Builder')

__all__ = ['build_site_map']

# Some site checks the user agent.
CRAWLER_REQUEST_HEADERS = {
    'User-Agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X10_10_1) AppleWebKit/537.36 (HTML, like Gecko) "
                   "Chrome/39.0.2171.95 Safari/537.36")
}


def _make_request(url):
    return requests.get(url, headers=CRAWLER_REQUEST_HEADERS)


def scrap_links_from_page(content, root):
    dom = lxml.html.fromstring(content)
    for link in dom.xpath('//a/@href'):
        if link.startswith(root):
            yield link


def get_links_from_site(path, links=[]):
    logger.debug("Request page {}".format(path))
    response = _make_request(path)
    if response.ok and response.headers.get('Content-Type').upper().startswith('TEXT/HTML'):
        _links = scrap_links_from_page(response.content, path)
        for l in _links:
            if l not in links:
                links.append(l)
                logger.debug("   * Link: {} added to collection.".format(l))
                get_links_from_site(l, links)
            else:
                logger.debug(" * Link: {} already scraped.. Ignoring.".format(l))

    return links


def build_site_links_list(url):
    return [l for l in get_links_from_site(url, [])]


def build_page_links_list(url):
    response = _make_request(url)
    return [l for l in set(scrap_links_from_page(response.content, url))]


def build_site_map(url):
    """
    :param url: url
    :return: sitemap.xml containing only the required <loc> information.
    """
    jinja_env = Environment(
        loader=PackageLoader('crawler', './'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = jinja_env.get_template('sitemap.xml')
    return template.render(links=build_site_links_list(url))
