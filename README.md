# Site Map Generator

## Description

This is a simple example on how to develop a application using some standards and libraries.
It provides a command line to automatically generate a simple sitemap.xml given a url.

The approach used to implement this application also aimed to show the usage of programming techniques and libraries usage.

## Capabilities

 * Should work on any site.
 * Follow all links recursively.
 * Does not follow links that were previouly visited.

## Limitations

 * The url provided on command line must include the schema (http://, https://) otherwise it will crash.
 * Does not follow redirect (HTTP 3xx).
 * Only scraps pages which response content-type is text/html.
 * Not performance optimized.
 * Can hang or even crash if the site was to many links and/or to many levels.

## Some Implementation Alternatives
 * Usage of an existent scrap oriented framework (e.g scrapy).
 * Usage of Beautiful Soup library to parse the html.
 * Usage of urllib3 instead of requests.
 * Usage of another template language like Mako, Chameleon or not even use one and generate it using python string manipulation.

## Setup
 * Clone the repository
    
        $ git clone https://github.com/debonzi/sitemapgen.git
        
 * Setup a virtualenv and activate it
    
        $ virtualenv .venv
        $ source .venv/bin/activate
        (.venv) $
        
 * Install the requirements and the sitemapgen package in develop mode
    
        (.venv) $ pip install -r requirements.txt
        (.venv) $ python setup.py develop


## Usage
    
        (.venv) $ mapgen --help
        Usage: mapgen [OPTIONS] URL

        Options:
            --debug  Run in Debug Mode.
            --help   Show this message and exit.

        (.venv) $ mapgen https://github.com/
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <url>
                <loc>
                    https://github.com/
                </loc>
            </url>
            <url>
                <loc>
                    https://github.com/about
                </loc>
            </url>
            <url>
                <loc>
                    https://github.com/blog
                </loc>
            </url>
            ...
            <url>
                <loc>
                    https://github.com/security
                </loc>
            </url>

        </urlset>
