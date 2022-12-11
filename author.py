import config
import urllib.request
import openai
from os.path import exists
from config import parsestory

def aiwrite(story):
    openai.api_key = config.OPENAI_API_KEY
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=story,
            temperature=0.8,
            max_tokens=800
        )
    return response

def aipaint(description):
    openai.api_key = config.OPENAI_API_KEY
    print(description)
    response = openai.Image.create(
                    prompt=description,
                    n=1,
                    size="512x512"
                    )
    image_url = response['data'][0]['url']
    return image_url

if exists('story.txt'):
    print("using cached story")
else:
    # write a new text
    print("Sending Request:" + config.FULLREQUEST)
    response=aiwrite(config.FULLREQUEST)
    print("Saving Response:" +response.choices[0].text)
    with open('story.txt', 'w') as f:
        f.write(response.choices[0].text)

story=parsestory()

for page in story:
    pagenumber=int(page['page'])
    filename='images/output'+ (f"{pagenumber:02d}") +".jpg"

    if(exists(filename)):
        print(filename+" already exists")
    else:
        print("Painting...")
        try:
            print("Page "+str(pagenumber))
            print(page['text'])
            painting=aipaint(page['image'])
            print("Storing as "+filename)
            urllib.request.urlretrieve(painting, filename)
        except Exception as err:
            print("Paint "+filename+" failed")
            print(err)

print("Illustrations complete and paint has dried!")
print("Now run main.py to read " + config.STORY)
