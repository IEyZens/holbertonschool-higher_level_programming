document.querySelector("html")
const div = document.getElementById("add_item").onclick = function() {listFunction()};

function listFunction() {
  const ul = document.getElementsByClassName("my_list");
  for (let i = 0; i < ul.length; i++) {
    const li = document.createElement("li");
    li.appendChild(document.createTextNode("Item"));
    ul[i].appendChild(li);
  }
}
