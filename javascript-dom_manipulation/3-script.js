document.querySelector("html")
const div = document.getElementById("toggle_header").onclick = function() {toggleFunction()};

function toggleFunction() {
  const header = document.getElementsByTagName("header");
  if (header[0].className == "red") {
    header[0].className = "green";
  } else {
    header[0].className = "red";
  }
}
