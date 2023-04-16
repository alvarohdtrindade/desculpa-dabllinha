from flask import Flask, render_template
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    # Define as mensagens de bom dia em cada idioma
    mensagens = {
        "en": "Good morning Dabla! You are the love of my life. Forgive me for seeming weird to you",

        "fr": "Bonjour Dabla ! Tu es l'amour de ma vie. Pardonne-moi de te paraitre bizarre",

        "de": "Guten Morgen Dabla! Du bist die Liebe meines Lebens. Verzeihen Sie mir, dass ich Ihnen komisch vorkomme",

        "it": "Buongiorno Dabla! Tu sei l'amore della mia vita. Perdonami se ti sembro strano",

        "es": "¡Buenos días Dabla! Eres el amor de mi vida. Perdóname por parecerte raro",
        
        "ru": "Добрый день, Дабла! Ты любовь моей жизни. Прости, что я показался тебе странным",

        "pt": "Bom dia Dablla! Você é o amor da minha vida. Me perdoe por parecer estranho com você"
    }

    # Cria um objeto do tradutor do Google
    translator = Translator()

    # Traduz a mensagem para cada idioma
    traducoes = {}
    for idioma, mensagem in mensagens.items():
        traducao = translator.translate(mensagem, dest=idioma.lower())
        traducoes[idioma] = traducao.text

    # Renderiza o template HTML e exibe as traduções
    return render_template('index.html', traducoes=traducoes)

if __name__ == '__main__':
    app.run()
    