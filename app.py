from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def home():
    # Get prompts/questions from the story
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story', methods=['POST'])
def generate_story():
    # Get answers from the form
    answers = {prompt: request.form[prompt] for prompt in story.prompts}
    # Generate the story
    generated_story = story.generate(answers)
    return render_template('story.html', story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)

