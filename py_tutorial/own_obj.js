#!/usr/bin/node

const myObj = {
  name: 'Abdul',
  nationality: 'Nigerian',
  genre: 'Hip Hop',
  members: 10,
  formed: 1992,
  [condition() ? 'split' : 'split']: condition() ? 2020 : false,
  
  albums: [
    {
      name: 'Africa Giant',
      released: 2019
    },
    {
      name: 'Love Daminy',
      released: 2022
    }
  ]
};

function condition () {
  return true;
}


const bandInfo = `Hello, this is ${myObj.name} and our band was formed in ${myObj.formed}, presently we have in our band ${myObj.members} members. Please note that our genre is ${myObj.genre}. Splitted? (${myObj.split}). ${myObj.albums[0].name}`;
console.log(bandInfo);
