#word/line counter
import sys

def countLines(data):
    lines = data.split("\n")
    for i in lines:
        if len(i) == 0: #check if line is blank
            lines.remove(i) #remove blank lines
    return len(lines)

def countWords(data):
    words = data.split(" ")
    return len(words)

if __name__ == "__main__": #only run the code below if running from command line, if imported this section won't run
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file>")
        exit(1)
    
    fileName = sys.argv[1] #filename read will always be second value
    f = open(fileName, "r")
    data = f.read()
    f.close()

    numLines = countLines(data)
    numWords = countWords(data)

    print("Line Count: ", numLines)
    print("Word Count: ", numWords)