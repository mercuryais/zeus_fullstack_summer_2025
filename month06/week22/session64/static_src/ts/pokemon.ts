console.log("Pokemon API call");

interface Pokemon {
    name: string;
    id: number;
    sprites: {
        front_default: string;
    };
    types: Array<{
        name: string;
    }>;
}

async function fetchPokemon(pokemonName: string): Promise<void> {
    try {
        console.log(`Fetch data for ${pokemonName}`);

        const url = `https://pokeapi.co/api/v2/pokemon/${pokemonName.toLowerCase()}`;

        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Pokemon not found! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Success');
        console.log(`Name: ${data.name.toUpperCase()}`);
        console.log(`ID: ${data.id}`);
        console.log(`Types: ${data.types[0]?.type.name}`);
        console.log(`See the sprite: ${data.sprites.front_default}`);
        
        const pokemonDiv = document.getElementById('pokemon');

        const pokeName = document.createElement('p');
        pokeName.textContent = data.name.toUpperCase();
        pokemonDiv?.appendChild(pokeName);

        const pokemonId = document.createElement('p');
        pokemonId.textContent = `${data.id}`;
        pokemonDiv?.append(pokemonId);

        const pokemonImage = document.createElement('img');
        pokemonImage.src = data.sprites.front_default;
        pokemonDiv?.appendChild(pokemonImage)
    } catch (error) {
        console.error(`Error fetching ${pokemonName}: `,error)
    }
}

fetchPokemon("pikachu");