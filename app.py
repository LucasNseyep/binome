import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(question),
            temperature=0,
            max_tokens=500,
            # top_p=1,
            # frequency_penalty=0.0,
            # presence_penalty=0.0,
            # stop=["\n"]
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(question):
    return """{}
Here's what the above object is doing:""".format(question)
