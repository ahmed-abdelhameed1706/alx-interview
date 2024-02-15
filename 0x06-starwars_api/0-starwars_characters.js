#!/usr/bin/node
const request = require('request');

const movieNumber = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + movieNumber;

request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    const name = await new Promise((resolve, reject) => {
      request(character, function (error, response, body) {
        if (error) {
          reject(error);
        }
        resolve(JSON.parse(body).name);
      });
    });
    console.log(name);
  }
});
