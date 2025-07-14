document.querySelector("html")

window.onload = function () {
  const div = document.getElementById("hello");
  fetchAPI(div);
}

async function fetchAPI(div) {
  const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  let file = await fetch(url);
  let translate = await file.json();
  div.innerHTML = translate.hello;
}
