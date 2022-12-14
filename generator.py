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
    prompt=image_prompt +"realistic high resolution",
    n=1,
    size="256x256"
  )
  image_url = image_generator['data'][0]['url']
  text_string = text_generator["choices"][0]["text"]
  
  #text_string = "Once upon a time, far away in the magical kingdom of Belgium, there lived a group of mischievous monkeys. The monkeys were always up to some kind of mischief, and often caused trouble for the people of Belgium. One day, the monkeys decided that they wanted to take over Belgium and rule the kingdom as their own. At first, the people of Belgium laughed at the idea of monkeys conquering their kingdom, but the monkeys were determined to make their dream come true. They began to organize themselves and plan out their strategy for taking over. First, the monkeys created an army of their own to protect them from any opposition. Then, they set up a government with a leader and laws that would ensure their success. Finally, the monkeys declared war on Belgium and began their conquest. The people of Belgium were shocked and scared, but they fought bravely against their monkey foes. The battle raged on for days, with neither side gaining any advantage. Eventually, however, the monkeys emerged victorious, and Belgium was under the rule of the monkeys. The monkeys were quick to make changes to their new kingdom. They built schools and universities to educate their citizens, and they established a strong economy with plenty of jobs. Soon, the monkeys had become beloved leaders of the Belgian people. And so, the monkeys ruled Belgium for many years, bringing peace and prosperity to the land. The people of Belgium never forgot the brave monkeys who conquered their kingdom, and they still tell stories about the great monkey rulers to this day."

  #image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Lleyton_Hewitt_%28AUS%29_%2821426427855%29.jpg/1920px-Lleyton_Hewitt_%28AUS%29_%2821426427855%29.jpg"

  # print the completion
  return image_url, text_string