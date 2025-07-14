document.querySelector("html")
const div = document.getElementById("red_header").onclick = function() {clickFunction()};

function clickFunction() {
  const header = document.getElementsByTagName("header");
  for (let i = 0; i < header.length; i++) {
    header[i].classList.add("red");
  }
}
