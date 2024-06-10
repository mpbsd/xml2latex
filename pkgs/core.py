#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs


def main():
    with open("brew/input.html", "r") as raw_html_file:
        html = raw_html_file.read()
        soup = bs(html, 'lxml')
        for question in soup.find_all('div', {'class': 'question'}):
            print(question)


if __name__ == "__main__":
    main()
