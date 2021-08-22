import requests


def return_cep(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    return response.json()


def return_pokemon(pokemon):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon))
    return response.json()['sprites']['front_shiny']


def return_generic_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    print(return_cep("61801670"))
    print("See your chosen pokemon: {}".format(return_pokemon("pikachu")))
    print(return_generic_response("https://www.google.com"))
