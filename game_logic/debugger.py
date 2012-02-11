## A cool debugger
## Simple, and easy, and I guess effective, joy

## Made by Thomas Gull

class Debug: # Just a little debugger, if debug file is empty then the debugger will just "print output"
    def __init__(self, on_off, debug_file=''):
        self.on_off = on_off
        if debug_file != '':
            self.debug_file = open(debug_file, 'w')
        else:
            self.debug_file = ''
    def setFile(self, new_file):
        if debug_file != '':
            self.debug_file.close()
            self.debug_file = open(new_file, 'w')
        else:
            self.debug_file = open(new_file, 'w')
    def setOn(self):
        self.on_off = True
    def setOff(self):
        self.on_off = False
    def write(self, message):
        if self.debug_file != '':
            self.debug_file.write(message)
        else:
            print message
    def close(self):
        if self.debug_file != '':
            self.debug_file.close()
            return True
        else:
            return True

DEBUGGER = Debug(True)
# Just use with from debugger import *
# then just DEBUGGER.write('whatever you want to display')

def main():
    print "Well, what did you expect?"
    print "This is better used if imported to other programs."
    print "like, import debugger?"

if __name__ == '__main__':
    main()
