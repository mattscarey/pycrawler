__author__ = 'Matthew'

class Data:

    def __init__(self, output):
        self.wordsCount = 0
        self.output = output
        self.wordDict = {}
        self.associations = {}

    def customStrip(self, text):
        ret = text
        charactersReplacedBySpace = ["\n", "\t", "     ", "   "]
        charactersRemoved = [",", "." ,")", "(", ":", ";", "'", '"', "?", "!", "[", "]", " -"]
        for char in charactersReplacedBySpace:
            ret = ret.replace(char, " ")
        for char in charactersRemoved:
            ret = ret.replace(char, "")
            ret = ''.join([i for i in ret if not i.isdigit()])
        return ret.lower()

    def getWords(self, rawHTML):
        paragraphsRaw = rawHTML.split("<p>")
        fullText = ""
        paragraphs = []
        for paragraph in paragraphsRaw:
            paragraphs.append(paragraph.split("</p>")[0])
        for paragraph in paragraphs:
            text = ""
            tagPieces = paragraph.split("<")
            for piece in tagPieces[1:len(tagPieces) - 10]:
                temp = self.customStrip(piece.split(">")[1])
                text += temp
            if "jquery" not in text:
                fullText += " " + text

        return fullText.split(" ")

    def addSurrounding(self, word, surrounding):
        for wordSurr in surrounding:
            try:
                self.associations[word][wordSurr] += 1
            except:
                self.associations[word][wordSurr] = 1

    def add(self, word, surrounding):
        self.wordsCount += 1
        try:
            self.wordDict[word] += 1
            self.addSurrounding(word, surrounding)
        except:
            self.wordDict[word] = 1
            self.associations[word] = {}

    def printList(self):
        with open(self.output, 'w') as f:
            for word in self.wordDict.keys():
                count = self.wordDict[word]
                associatedWords = self.associations[word]
                f.write('|||' + word + ':' + '\n')
                for assoc in self.associations[word]:
                    assocCount = associatedWords[assoc]
                    percent = str(round(float((float(assocCount) / count) * 100.00), 2))
                    f.write('   ' + word + ' -> ' + assoc + '||, ' + percent)
                    f.write('\n')

    def getData(self, rawHTML):
        words = self.getWords(rawHTML)
        for i in range(1, len(words) - 1):
            if words[i] != "" and words[i - 1] != "" and words[i + 1] != "":
                self.add(words[i], [words[i - 1], words[i + 1]])

    def dump(self):
        self.printList()

    def end(self):
        print("total words: " + str(self.wordsCount))
        print("total unique words: " + str(len(self.wordDict.keys())))
        self.printList()