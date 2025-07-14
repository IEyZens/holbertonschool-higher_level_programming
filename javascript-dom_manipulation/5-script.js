document.querySelector("html")
const div = document.getElementById("update_header").onclick = function() {headerFunction()};

function headerFunction() {
  const header = document.getElementsByTagName("header");
  for (let i = 0; i < header.length; i++) {
    header[i].innerHTML = "New Header!!!";
  }
}
