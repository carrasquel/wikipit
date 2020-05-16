# -*- coding: utf-8 -*-
# wikipit.py

import wikipedia
import click

@click.command()
@click.argument('search')
@click.option('--browser', '-b', default=False, help="Open in browser.")
@click.option('--lines', '-l', default=15, help="Open in browser.")
def wiki(search, browser, lines):

    result = wikipedia.summary(search)

    print(result)


if __name__ == "__main__":

    # search = "Miguel Cabrera"

    # result = wiki(search)

    # print(result)

    wiki()

