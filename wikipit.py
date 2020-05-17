# -*- coding: utf-8 -*-
# wikipit.py

import shutil
import textwrap
import webbrowser

import wikipedia
import click

@click.command()
@click.argument('search')
@click.option('--lines', '-l', default=10, help="Number of lines.")
@click.option('--all', '-a', is_flag=True, help="Print the entire page content.")
@click.option('--browser', '-b', is_flag=True, help="Open in browser.")
@click.option('--lang', '-e', default="en", help="Open in browser.")
def wiki(search, lines, all=None, browser=None, lang="en"):

    wikipedia.set_lang(lang)
    
    if browser:
        page = wikipedia.page(search)
        url = page.url

        webbrowser.open(url, autoraise=True)

        return
    
    result = wikipedia.summary(search)

    if all:
        page = wikipedia.page(search)
        print(page.content)

        return

    if lines:
        sizes = shutil.get_terminal_size((80, 20))
        columns = sizes.columns
        columns -= 2

        rows = textwrap.wrap(result, columns)

        for row in rows[0:lines]:
            print(row)

    else:
        print(result)


if __name__ == "__main__":

    wiki()
