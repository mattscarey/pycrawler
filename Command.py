__author__ = 'Matthew'

import time
import os

class Command:

    def __init__(self):
        self.root = os.path.dirname(os.path.abspath(__file__)) + "/"
        self.command = self.root + 'command.txt'
        self.response = self.root + 'response.txt'
        self.running = True
        self.start()

    def getText(self, file):
        ret = ""
        with open(file, "r") as f:
            for line in f:
                ret += line
        return ret

    def start(self):
        while self.running:
            command = raw_input("Enter Command: ")
            with open(self.command, "w") as com:
                com.write(command)
            time.sleep(.5)
            responses = self.getText(self.response).split("\n\n")
            print(responses[len(responses) - 1])
            keepGoing = raw_input("Enter Another command? y or n: ")
            if keepGoing == "n":
                self.running = False

if __name__ == "__main__":
    command = Command()