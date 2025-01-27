let next = document.getElementById("next");
let prev = document.getElementById("prev");
let sizeDiv = document.getElementById("sizeDiv").offsetWidth;
let slider = document.getElementById("slider");

function goNext() {
  slider.style.transition = "transform 0.5s ease-in-out";
  slider.style.transform = "translateX(-" + sizeDiv + "px)";
  setTimeout(() => {
    slider.appendChild(slider.firstElementChild);
    slider.style.transition = "none";
    slider.style.transform = "translateX(0)";
  }, 500);
}

function goBack() {
  slider.style.transition = "transform 0.5s ease-in-out";
  slider.style.transform = "translateX(" + sizeDiv + "px)";
  setTimeout(() => {
    slider.insertBefore(slider.lastElementChild, slider.firstElementChild);
    slider.style.transition = "none";
    slider.style.transform = "translateX(0)";
  }, 500);
}

function startMarquee() {
  setInterval(goNext, 5000);
}

next.addEventListener("click", goNext);
prev.addEventListener("click", goBack);
startMarquee();