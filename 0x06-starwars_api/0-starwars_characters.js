#!/usr/bin/node
const request = require('request');

const movieNumber = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + movieNumber;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
