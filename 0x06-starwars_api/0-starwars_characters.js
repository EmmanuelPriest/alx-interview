#!/usr/bin/node
'use strict';

/* Importing the request module */
const request = require('request');

/* Store movie ID from command line arguments */
const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    respRequestReturn(characters, 0);
  }
});

function respRequestReturn (character, idx) {
  request(character[idx], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      if (idx + 1 < character.length) respRequestReturn(character, ++idx);
    }
  });
}
