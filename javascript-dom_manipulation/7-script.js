document.querySelector("html")
const div = document.getElementById("list_movies");

async function fetchAPI() {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  let file = await fetch(url);
  let movies = await file.json();
  for (let i = 0; i < movies.results.length; i++) {
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(movies.results[i].title));
    div.appendChild(li);
  }
}

fetchAPI()
