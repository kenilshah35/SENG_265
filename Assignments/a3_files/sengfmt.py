#!/usr/bin/env python3

# File: sengfmt.py
# Student Name  : Kenil Shah
# Student Number: V00903842
# SENG 265 - Assignment 2

import argparse
import sys
import fileinput

fmt = True
maxWidth = 0
mrgn = 0
lineSize = 0
newLine = False
caps = False
res = []

def main ():

    output = ""
    lines = [line for line in fileinput.input()]
    if(lines[-1] != '\n'):
        lines.append('\n')

    processed = [process(line) for line in lines]

    trimEmpty = [line for line in processed if line != None]

    if(len(trimEmpty) == 0):
        return
    else:
        output = "".join(trimEmpty)
        print(output.rstrip('\n'))

def process(line):

    global fmt, maxWidth, mrgn, lineSize, newLine, caps, res

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
                mrgn = mrgn + int(split[1][1:])
                #fmt = True
            elif(split[1][:1] == "-"):
                mrgn = mrgn - int(split[1][1:])
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

        #print(mrgn)
        out =""

        #Empty Line
        if(maxWidth == 0):

            if(split == []):
                lineSize = 0
                if(newLine == True):
                    return '\n'
                else:
                    newLine = True
                    return '\n'
            newLine = False

        # caps on
        if(caps == True):
            count = 0
            for x in split:
                split[count] = x.upper()
                count = count + 1

        # adding words to the line in case max width is not provided
        if(maxWidth == 0):
            #print("I was here")
            # Setting margin
            if(lineSize == 0):
                out = "".join([" " for i in range(mrgn)])
            lineSize = mrgn

            out = out + line
            lineSize = 0
            return out

        else:
            #print(mrgn)
            for o in split:
                res.append(o)

            if split == []:

                answerLast =[]
                answerLast = justify(res,maxWidth - mrgn)
                #print(mrgn)

                margin = "".join([" " for l in range(mrgn)])

                #printing out
                for something in answerLast:
                    out = out + margin + something + '\n'
                res = []

                return out + '\n'

    else:
       # line = line + '\n'
        return line

def justify(wordList,maxWidth):
    numChars = len(wordList)
    start = 0
    end = 0
    counter = 0
    sizeOfLine=0
    answer = []

    while(True):
        counter = start
        if(counter >= numChars):
            break
        sizeOfLine = 0

        while(counter < numChars):
            sizeOfLine = sizeOfLine + len(wordList[counter])

            if(counter != start):
                sizeOfLine = sizeOfLine + 1
            if(sizeOfLine > maxWidth):
                break
            counter = counter + 1

        end = counter - 1
        if(start == end):
            str = wordList[start]
        else:
            if(counter != numChars):
                sizeOfLine = sizeOfLine - len(wordList[counter]) - 1
            numWords = end - start + 1
            totalspaces = maxWidth - (sizeOfLine - (numWords - 1))
            spaces = totalspaces // (numWords - 1)
            additionalSpaces = totalspaces % (numWords - 1)
            str = ""

            for i in range(start, end):
                str = str + wordList[i] + " "*spaces
                if i - start < additionalSpaces:
                    str = str + " "
            str = str + wordList[end]

        answer.append(str)
        start = counter

    return answer

if __name__ == "__main__":
    main()
