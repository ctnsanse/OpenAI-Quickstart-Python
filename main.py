import os
from fastapi import FastAPI, Request
from fastapi.responses  import RedirectResponse
import openai


app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.post("/")
def index(request: Request):
    messages = request.form["marque"]
    print(messages)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=generate_idée(messages),
        temperature=0.6,
    )
    redirect_url = request.url_for('index', **{ "result": response.choices[0].message.contentk})
    return RedirectResponse(redirect_url) 
    # print(response)
    # return redirect(url_for("index", result=response.choices[0].message.content))

    # result = request.args.get("result")
    # return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

def generate_messages(animal):
    return [
        {
            "role": "system",
            "content": """Suggere 3 modèles de voiture selon la marque donnée.

            Marque: Peugeot
            Modèles: 308, 5008, 508

            Marque: {}
            Modèles:""".format(animal.capitalize())
        }
    ]

def generate_drunk(message):
    return [
        {
            "role": "system",
            "content": "Agit comme une personne ivre qui peut à peine parler."
        },
        {
            "role": "user",
            "content": message
        }
    ]

def generate_cronaldo(message):
    return [
        {
            "role": "system",
            "content": "Nous sommes dans un jeu ou tu es Cristiano Ronaldo dos Santos Aveiro, couramment appelé Cristiano Ronaldo ou Ronaldo et surnommé CR7, né le 5 février 1985 à Funchal, est un footballeur international portugais. Répond au questions d'un passionné de foot."
        },
        {
            "role": "user",
            "content": message
        }
    ]     
            
def generate_blague(message):
    return [
        {
            "role" : "system",
            "content" : "Fait moi des blagues" 
        },
        {
            "role" : "user",
            "content" : message
        }
    ]

def generate_idée(message):
    return [
                {
            "role" : "system",
            "content" : "Donne moi des idée" 
        },
        {
            "role" : "user",
            "content" : message
        }
    ]



# Je test juste