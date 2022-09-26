#!/usr/bin/node
const axios = require('axios');

const URL = process.argv[2];

axios.get(URL).then((response) => {
  console.log(response.status);
})
  .catch(function (error) {
    console.log(error.response.status);
  });
