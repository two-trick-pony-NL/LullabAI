from flask import Flask, render_template, request
import flask
from generator import generator

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if flask.request.method == 'POST':
        prompt = request.form['prompt']
        image, text = generator(prompt)
        return render_template('result.html', title=prompt, image=image, text=text)
    
    else:
        prompt = "A dog that wanted to fly"
        #image, text = generator(prompt)
        text = "bla bla bla Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam neque felis, feugiat eu velit non, congue pretium purus. Nullam in egestas magna, ac tincidunt est. Sed pellentesque non arcu a pulvinar. Suspendisse tristique, arcu eget viverra euismod, nisi tellus vehicula ipsum, eu volutpat urna neque eu arcu. Nam semper, odio in consequat ultrices, diam nibh aliquet purus, in placerat elit arcu vitae arcu. Nulla nec tortor aliquam, varius libero vel, faucibus leo. Nulla at nulla et nisi bibendum eleifend. Curabitur venenatis felis sed pretium consequat. Suspendisse at sem congue, suscipit turpis in, malesuada diam. Sed sed sapien non sem gravida sodales ac id nisl. Sed a nisl a justo faucibus pellentesque vitae vel turpis. Vivamus blandit mauris metus, sit amet iaculis sem volutpat at. Vestibulum rhoncus et mauris eget aliquam. Fusce tincidunt magna quis enim tincidunt, in auctor turpis elementum. Donec eget nunc id odio interdum ultrices porta quis tellus. Nulla vehicula arcu vitae erat finibus auctor."
        image = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-6XpuzVE6XXqjlKPaUSDEySrK/user-ILZ9gsbszaPrRbBIFkxMBh88/img-NnR4pHbrMLg9u14mym7hP4US.png?st=2022-12-14T13%3A57%3A56Z&se=2022-12-14T15%3A57%3A56Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-14T09%3A49%3A44Z&ske=2022-12-15T09%3A49%3A44Z&sks=b&skv=2021-08-06&sig=tYk9GufniVUV6S%2BfqSjusandmIbVyzMUkZaXUYVClV0%3D"
        return render_template('start.html', title=prompt, image=image, text=text)