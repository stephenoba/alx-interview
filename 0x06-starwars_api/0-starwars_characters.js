#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

function fetchCharacterName (characterURL) {
  return new Promise((resolve, reject) => {
    request(characterURL, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body).name);
    });
  });
}

request(url, async (error, response, body) => {
  if (error) {
    console.error('Error fetching the movie:', error);
    return;
  }

  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    try {
      const name = await fetchCharacterName(characters[i]);
      console.log(name);
    } catch (err) {
      console.error('Error fetching character:', err);
    }
  }
});
