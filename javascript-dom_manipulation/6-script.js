document.querySelector("html")
const div = document.getElementById("character");

async function fetchAPI() {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  let file = await fetch(url);
  let character = await file.json();
  div.innerHTML = character.name;
}

fetchAPI()
