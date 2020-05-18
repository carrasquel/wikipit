# -*- coding: utf-8 -*-
# wikipit.py

from functools import partial

import shutil
import textwrap
import webbrowser

import wikipedia
import click

OFFSET = 2

def delegate_to_browser(address):
    webbrowser.open(address, autoraise=True)

def display_raw(content):
    print(content)

def display_with_fixed_width(lines, content):
    sizes = shutil.get_terminal_size((80, 20))
    columns = sizes.columns - OFFSET

    rows = textwrap.wrap(content, columns)

    for row in rows[0:lines]:
        print(row)

def address_from_keywords(keywords):
    return wikipedia.page(keywords).url

def summary_from_keywords(keywords):
    return wikipedia.summary(keywords)

def content_from_keywords(keywords):
    return wikipedia.page(keywords).content

def searcher(keywords, lines, all_, browser):
    if browser:
        return address_from_keywords(keywords)
    if all_:
        return content_from_keywords(keywords)

    result = summary_from_keywords(keywords)

    return result


@click.command()
@click.argument('keywords')
@click.option('--lines', '-l', default=10, help="Number of lines.")
@click.option('--all', '-a', 'all_', is_flag=True, help="Print the entire page content.")
@click.option('--browser', '-b', is_flag=True, help="Open in browser.")
@click.option('--lang', '-e', default="en", help="Open in browser.")
def wiki(keywords, lines, all_=None, browser=None, lang="en"):

    wikipedia.set_lang(lang)

    display = display_raw
    if browser:
        display = delegate_to_browser
    elif not all_ and lines:
        display = partial(display_with_fixed_width, lines)
    
    display(searcher(keywords, lines, all_, browser))


if __name__ == "__main__":

    wiki()
