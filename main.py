from flask import *
from flask_bootstrap import Bootstrap
from PokeStat import PokeStat
import requests

# Initialize Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


#Initialize Variables
poke_url = 'https://pokeapi.co/api/v2/pokemon/'
titles = PokeStat('Name', 'HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed', 'ffffff')
pokelist = []
type_to_color_dict = {
    'normal': '#f5eace',
    'fire': '#ff0000',
    'water': '#0000ff',
    'grass': '#487e65',
    'rock':'#9e915c',
    'poison':'#6630a6',
    'ground':'#8e8252',
    'fairy':'#ffb6c1',
    'steel': '#cac8d0',
    'dark': '#201d28',
    'psychic': '#e97a9d',
    'electric':'#cccc7a',
    'ice':'#bcf4e2',
    'flying': '#e3e4ff',
    'dragon': '#9345ee',
    'bug': '#63614e',
    'fighting': '#86476B',
    'ghost': '#3a1b5f'
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon', 'empty')
        response = requests.get(f'{poke_url}{pokemon.lower()}')

        if response.text == 'Not Found':
            print('Trump Won')
            flash('Go Find God.  Come Back When You Found God.')
        else:
            poke_json = response.json()

            name = poke_json['name']
            hp = poke_json['stats'][0]['base_stat']
            attack = poke_json['stats'][1]['base_stat']
            defense = poke_json['stats'][2]['base_stat']
            spat = poke_json['stats'][3]['base_stat']
            spdf = poke_json['stats'][4]['base_stat']
            speed = poke_json['stats'][5]['base_stat']

            element = poke_json['types'][0]['type']['name']

            color = type_to_color_dict[element]

            new_poke = PokeStat(name, hp, attack, defense, spat, spdf, speed, color)
            print(f'Conjuring up a new Pokemon, {new_poke.name}, in the color {new_poke.color}, with base stats {new_poke.hp}, {new_poke.attack}, {new_poke.defense}, {new_poke.spat}, {new_poke.spdf}, {new_poke.speed}')
            pokelist.append(new_poke)

        return redirect(url_for('home', titles=titles, pokelist=pokelist))
    return render_template('home.html', titles=titles, pokelist=pokelist)













if __name__ == '__main__':
    app.run(debug=True)