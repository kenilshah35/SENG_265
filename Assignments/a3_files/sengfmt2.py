#!/opt/local/bin/python

import sys
import fileinput
from formatter import Formatter

def main():
    """
    Creates an instance of the formatter and process the lines
    """

    rawData = [line for line in fileinput.input()]
    if rawData[-1] != '\n':
        rawData.append('\n')

    formatter = Formatter(inputlines = rawData )

    lines = formatter.get_lines()

    output = "".join(lines)
    if lines != "":
        print(output.rstrip('\n'))
    else:
        return


if __name__ == "__main__":
    main()
