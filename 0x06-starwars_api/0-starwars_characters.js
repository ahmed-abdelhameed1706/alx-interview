#!/usr/bin/node
const request = require("request");

const movie_number = process.argv[2];

const url = "https://swapi-api.hbtn.io/api/films/" + movie_number;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
