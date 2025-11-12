console.log("TypeScript-ээс мэндчилье! 🚀 ");
function main() {
  fetchPokemons();
}

type IPokemon = {
  name: string;
  url: string;
}

interface IPokemonDetail {
  id: string,
  sprites: {
    other: {
      "official-artwork": {
        front_default: string;
      }
    }
  }
}

async function fetchPokemons(): Promise<void> {
    const POKEMONS_URL: string = 'https://pokeapi.co/api/v2/pokemon/?limit=0&offset=10';

    const result = await fetch(POKEMONS_URL);
    const data = await result.json();
    const results = data.results as [IPokemon];
    const pokemonContainerElement = document.getElementById('pokemon-container');

    for (let i = 0; i < results.length; i++){
      const pokemonName = results[i].name;
      const pokemonNameElement: HTMLParagraphElement = document.createElement('p');
      pokemonNameElement.textContent = pokemonName;
      pokemonNameElement.classList.add('pokemon-name')

      const pokemonDetails = await fetch(results[i].url);
      // console.log(pokemonDetails);
      const pokemonDetailsData: IPokemonDetail = await pokemonDetails.json();
      console.log(pokemonDetailsData);
      const pokemonImage: HTMLImageElement = document.createElement('img');
      pokemonImage.src = pokemonDetailsData.sprites.other["official-artwork"].front_default;
      pokemonImage.classList.add('pokemon-image')

      const pokemonID: HTMLParagraphElement = document.createElement('p');
      if(parseInt(pokemonDetailsData.id) < 10) {
        pokemonID.textContent = "#00" + pokemonDetailsData.id
      } else if (parseInt(pokemonDetailsData.id) < 100) {
        pokemonID.textContent = "#0" + pokemonDetailsData.id
      } else {
        pokemonID.textContent = "#" + pokemonDetailsData.id
      }
      pokemonID.classList.add("pokemon-id")

      const pokemonContainer: HTMLDivElement = document.createElement('div');
      pokemonContainer.classList.add('pokemon-single-container')
      pokemonContainer?.appendChild(pokemonImage);
      pokemonContainer?.appendChild(pokemonNameElement);
      pokemonContainer?.appendChild(pokemonID);
      pokemonContainerElement?.appendChild(pokemonContainer)
    }
}





document.addEventListener("DOMContentLoaded", main);