#!/usr/bin/env python3 

# File: sengfmt.py 
# Student Name  : Kenil Shah
# Student Number: V00903842
# SENG 265 - Assignment 2

import argparse
import sys

fmt = True
maxWidth = 0
mrgn = 0
lineSize = 0
newLine = False
caps = False
res =[]

def main():

    str = "?maxwidth 24\n?mrgn 4\nWhat must be acknowledgment should be\n\nor well don't, it's not like you have to\n\n"

    output = ""
    lines = [line for line in str.split('\n')]
    lines.append('\n')
    processed = [process(line) for line in lines]
    trimEmpty = [line for line in processed if line != None]

    if(len(trimEmpty) == 0):
        return
    else:
        output = "".join(trimEmpty)
        print(output.rstrip('\n'))

def process(line):

    global fmt, maxWidth, mrgn, lineSize, newLine, caps,res

    split = line.split()

    if(len(split) != 0):

        if(split[0] == "?fmt"):
            if(split[1] == "off"):
                fmt = False
            elif(split[1] == "on"):
                fmt = True
            return None

        if(split[0] == "?cap"):
            if(split[1] == "off"):
                caps = False
            elif(split[1] == "on"):
                caps = True
            return None

        if(split[0] == "?maxwidth"):
            if(isinstance(int(split[1]),int)):
                maxWidth = int(split[1])
                fmt = True
            return None

        if(split[0] == "?mrgn"):
            if(split[1][:1] == "+"):
                mrgn += int(split[1][1:])
                #fmt = True
            elif(split[1][:1] == "-"):
                mrgn -= int(split[1][1:])
                #fmt = True
                if(mrgn < 0):
                    mrgn = 0
            else:
                mrgn = int(split[1])
                #fmt = True
            if(maxWidth != 0):
                if(mrgn > maxWidth - 20):
                    mrgn = maxWidth -20
            return None


    if(fmt == True):

        out =""
        #Empty Line
        """
        if(split == []):
            if(newLine):
                return '\n'
            else:
                newLine = True
                return '\n\n'
        newLine = False
        """

        # caps on
        if(caps == True):
            count = 0
            for x in split:
                split[count] = x.upper()
                count += 1


        # adding words to the line in case max width is not provided
        if(maxWidth == 0):

            # Setting margin
            if(lineSize == 0):
                out = "".join([" " for i in range(mrgn)])
            lineSize = mrgn

            out += line
            lineSize = 0
            return out

        else:
            for o in split:
                res.append(o)
            #print(res)

            if split == []:
                answerLast = []
                answerLast = justify(res,maxWidth-mrgn)

                margin = "".join([" " for i in range(mrgn)])

                for something in answerLast:
                    out = out + margin + something + '\n'
                res = []

                return out+'\n'

    else:
        #line += '\n'
        return line

def justify(words,maxWidth):
    num_of_words = len(words)
    start_ind, end_ind, runner = 0, 0, 0
    len_of_line, word_num_line = 0, 0
    answer = []

    while True:
        runner = start_ind
        if runner >= num_of_words:
            break
        len_of_line, word_num_line = 0, 0

        while runner < num_of_words:
            len_of_line = len_of_line + len(words[runner])
            word_num_line = word_num_line + 1
            if runner != start_ind:
                len_of_line = len_of_line + 1
            if len_of_line > maxWidth:
                break
            runner = runner + 1

        end_ind = runner - 1
        if start_ind == end_ind:
            oneline = words[start_ind] + " "*(maxWidth-len(words[start_ind]))
        else:
            if(runner != num_of_words):
                len_of_line = len_of_line - len(words[runner]) - 1
            word_num = end_ind - start_ind + 1
            extra_spaces = maxWidth - (len_of_line - (word_num - 1))
            basic_pad_spaces = extra_spaces // (word_num - 1)
            addition_pad_spaces = extra_spaces % (word_num - 1)
            oneline = ""

            for ind in range(start_ind, runner-1):
                oneline = oneline + words[ind] + " "*basic_pad_spaces
                if ind - start_ind < addition_pad_spaces:
                    oneline = oneline + " "
            oneline = oneline + words[runner-1]

        answer.append(oneline)
        start_ind = runner

    return answer


if __name__ == "__main__":
	main()
