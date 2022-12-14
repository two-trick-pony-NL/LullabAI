import openai
from configparser import ConfigParser

config = ConfigParser()
config.read('settings.env')
token = config.get('DEFAULT', 'openaikey')

openai.api_key = token

def generator(input):
  story_prompt = "Write me a bedtime story about a " + input
  image_prompt = "A "+input

  # create a completion
  text_generator = openai.Completion.create(
    model="text-davinci-003",
    prompt=story_prompt,
    temperature=0.7,
    max_tokens=360,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=1
  )
  image_generator = openai.Image.create(
    prompt=image_prompt +"cartoon style, cheerful",
    n=1,
    size="256x256"
  )
  image_url = image_generator['data'][0]['url']
  text_string = text_generator["choices"][0]["text"]

  # print the completion
  return image_url, text_string