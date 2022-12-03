#!/opt/local/bin/python

import sys
import re
import calendar

class Formatter:
    """This is the definition for the class"""

    def __init__(self, filename=None, inputlines=["?maxwidth 25","?mrgn 4","what must be acknowledged should be","\n","?mrgn +1","what must be acknowledged should be","\n"]):

        self.fmt = True
        self.maxWidth = 0
        self.mrgn = 0
        self.lineSize = 0
        self.newLine = False
        self.res = []
        self.replace = False
        self.toReplace = ""
        self.withReplace = ""
        self.monthAbbr = False

        self.inputlines = inputlines
        self.output = ""
        #print("in constructor\n")

        self.processed = [self.process(line) for line in self.inputlines]
        self.trimEmpty = [line for line in self.processed if line != None]

        if len(self.trimEmpty) != 0:
            self.output = "".join(self.trimEmpty)


    def process(self,line):

        split = line.split()

        if len(split) != 0:

            if split[0] == "?fmt":
                if split[1] == "off":
                    self.fmt = False
                elif split[1] == "on":
                    self.fmt = True
                return None

            if split[0] == "?maxwidth":
                if isinstance(int(split[1]) ,int):
                    self.maxWidth = int(split[1])
                    self.fmt = True
                return None

            if split[0] == "?mrgn":
                if split[1][:1] == "+":
                    self.mrgn += int(split[1][1:])
                elif split[1][:1] == "-":
                    self.mrgn -= int(split[1][1:])
                    if self.mrgn < 0:
                        self.mrgn = 0
                else:
                    self.mrgn = int(split[1])

                if self.maxWidth != 0:
                    if self.mrgn > (self.maxWidth - 20):
                        self.mrgn = self.maxWidth - 20
                return None

            if split[0] == "?replace":
                self.replace = True
                self.toReplace = split[1]
                self.withReplace = split[2]
                return None

            if split[0] == "?monthabbr":
                if split[1] == "on":
                    self.monthAbbr = True
                elif split[1] == "off":
                    self.monthAbbr = False
                return None

        if self.fmt == True:

            out = ""

            if self.maxWidth == 0:
                if split == []:
                    self.lineSize = 0
                    if self.newLine == True:
                        return '\n'
                    else:
                        self.newLine = True
                        return '\n'
                self.newLine = False

            if self.maxWidth == 0:
                if self.lineSize == 0:
                    out = "".join([" " for i in range(self.mrgn)])
                self.lineSize = self.mrgn

                out += line

                if self.replace == True:
                    out = re.sub(self.toReplace,self.withReplace,out)

                if self.monthAbbr == True:
                    out1 = re.search(r"(\d?\d)[\/\-\.](\d?\d)[\/\-\.](\d\d\d\d)",out)
                    if out1 != None:
                        out = re.sub(r"(\d?\d)[\/\-\.](\d?\d)[\/\-\.](\d\d\d\d)",calendar.month_abbr[int(out1.group(1))] + ". " + out1.group(2) + ", " +out1.group(3),out)

                self.lineSize = 0
                return out

            else:

                for i in split:
                    self.res.append(i)

                if split == []:
                    answerLast = []
                    answerLast = self.justify(self.res,self.maxWidth - self.mrgn)
                    margin = "".join([" " for i in range(self.mrgn)])

                    for someWords in answerLast:
                        out += margin + someWords + '\n'

                    if self.replace == True :
                        out = re.sub(self.toReplace,self.withReplace,out)
                        split1 = out.split()
                        answerLast1 = []
                        answerLast1 = self.justify(split1,self.maxWidth - self.mrgn)
                        margin1 = "".join([" " for i in range(self.mrgn)])
                        out = ""
                        for someWords1 in answerLast1:
                            out += margin1 + someWords1 + '\n'

                    if self.monthAbbr == True:

                        out1 = re.search(r"(\d?\d)[\/\-\.](\d?\d)[\/\-\.](\d\d\d\d)",out)
                        if out1 != None:
                            out = re.sub(r"(\d?\d)[\/\-\.](\d?\d)[\/\-\.](\d\d\d\d)",calendar.month_abbr[int(out1.group(1))] + ". " + out1.group(2) + ", " +out1.group(3),out)
                        split2 = out.split()
                        answerLast2 = []
                        answerLast2 = self.justify(split2,self.maxWidth - self.mrgn)
                        margin2 = "".join([" " for i in range(self.mrgn)])
                        out = ""
                        for someWords2 in answerLast2:
                            out += margin2 + someWords2 + '\n'

                    self.res = []

                    return out + '\n'

        else:
            return line

    def justify(self,wordList,width):
        numChars = len(wordList)
        start,end,counter,sizeOfLine = 0,0,0,0
        answer = []

        while True:
            counter = start
            if counter >= numChars:
                break
            sizeOfLine = 0

            while counter < numChars:

                sizeOfLine = sizeOfLine + len(wordList[counter])

                if counter != start:
                    sizeOfLine += 1
                if sizeOfLine > width:
                    break
                counter += 1

            end = counter - 1
            if start == end:
                str = wordList[start]
            else:
                if counter != numChars:
                    sizeOfLine = sizeOfLine - len(wordList[counter]) - 1
                numWords = end - start + 1
                totalSpaces = width - (sizeOfLine - (numWords - 1))
                spaces = totalSpaces // (numWords - 1)
                additonalSpaces = totalSpaces % (numWords - 1)
                str = ""

                for i in range(start,end):
                    str += wordList[i] + " "*spaces
                    if i - start < additonalSpaces:
                        str += " "
                str += wordList[end]

            answer.append(str)
            start = counter

        return answer


    def get_lines(self):
        return self.output

if __name__ == "__main__":

    format = Formatter()
    lines =  format.get_lines()
    print("".join(lines))
