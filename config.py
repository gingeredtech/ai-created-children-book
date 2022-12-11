import os
import re
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

PAGES = 10
WORDSPERPAGE=10
STORY = "The best Christmas ever!"
IMAGESTYLE = "Impressionist Painting"

CHAR1 = 'Ginger'
CHAR2 = 'Momo'

DESCRIBE1 = 'a ginger kitten'
DESCRIBE2 = 'a black kitten'

FORMAT = "For each page write PAGE then page number, then write TEXT and the page text then IMAGE followed by a description of an image to illustrate the page. Start each image description with A "+ IMAGESTYLE +" of ... "

FULLREQUEST = 'Write a '+ str(PAGES) + ' page children\'s story with no more than '+str(WORDSPERPAGE)+' words per page about ' + CHAR1 + ' who is a '+ DESCRIBE1 + \
    ' and ' + CHAR2 + ' who is a '+DESCRIBE2 + ". The title of the book is " + STORY + '. ' + FORMAT


def parsestory():
    with open('story.txt','r') as f:
        story=f.read()

    pages=[]
    regex = r"(PAGE) (\d+)([\s\S]*?)(TEXT)([\s\S]*?)(\w.+)([\s\S]*?)(IMAGE)([\s\S]*?)(\w.+)"
    matches = re.findall(regex, story) 
   
    for m in matches:
        illustration=m[9]
        illustration=illustration.replace(CHAR1,DESCRIBE1)
        illustration=illustration.replace(CHAR2,DESCRIBE2)
        pages.append({'page':m[1],'text': m[5],'image':illustration})
    
    return pages


