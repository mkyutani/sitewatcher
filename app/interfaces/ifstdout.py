#!/usr/bin/python3

from interfaces.ifprinter import BasePrinter

class Printer(BasePrinter):

    def __init__(self, args=None):
        pass

    def print(self, title, message, hash=None):
        if hash is None:
            print(' '.join([title, message]))
        else:
            print(' '.join([hash, title, message]))