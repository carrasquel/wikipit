# -*- coding: utf-8 -*-
# wikipit.py

import argparse
import wikipedia

def wiki(search):

    result = wikipedia.summary(search)

    return result


if __name__ == "__main__":

    search = "Miguel Cabrera"

    result = wiki(search)

    print(result)