# -*- coding: utf-8 -*-
# wikipit.py

from functools import partial

import shutil
import textwrap
import webbrowser

import wikipedia
import click


# Displayer

def delegate_to_browser(address):
    webbrowser.open(address, autoraise=True)

def display_raw(content):
    print(content)

def display_with_fixed_width(content, lines, offset=2):
    sizes = shutil.get_terminal_size((80, 20))
    columns = sizes.columns - offset

    rows = textwrap.wrap(content, columns)

    for row in rows[0:lines]:
        print(row)

def display_by_options(content, lines, all_, browser):
    method = display_raw
    if browser:
        method = delegate_to_browser
    elif not all_ and lines:
        method = partial(display_with_fixed_width, lines=lines)
    method(content)
    

# Searcher

def address_from_keywords(keywords):
    return wikipedia.page(keywords).url

def summary_from_keywords(keywords):
    return wikipedia.summary(keywords)

def content_from_keywords(keywords):
    return wikipedia.page(keywords).content

def search_by_options(keywords, all_, browser): # Kind of the Controller
    method = summary_from_keywords
    if browser:
        method = address_from_keywords
    elif all_:
        method = content_from_keywords

    return method(keywords)


# System

@click.command()
@click.argument('keywords')
@click.option('--lines', '-l', default=10, help="Number of lines.")
@click.option('--all', '-a', 'all_', is_flag=True, help="Print the entire page content.")
@click.option('--browser', '-b', is_flag=True, help="Open in browser.")
@click.option('--lang', '-e', default="en", help="Open in browser.")
def wiki(keywords, lines, all_=False, browser=False, lang="en"):

    # Config
    wikipedia.set_lang(lang)
    display = partial(display_by_options, lines=lines, all_=all_, browser=browser)
    search = partial(search_by_options, all_=all_, browser=browser)

    # Excecution
    display(search(keywords))


if __name__ == "__main__":

    wiki()
