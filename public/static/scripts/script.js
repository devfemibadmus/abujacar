var toggleOpen = document.getElementById("toggleOpen");
var toggleClose = document.getElementById("toggleClose");
var collapseMenu = document.getElementById("collapseMenu");

function toggleDropdown() {
  const dropdown = document.getElementById('popular_brand');
  dropdown.style.maxHeight = dropdown.style.maxHeight === '0px' ? '700px' : '0px';
}

function handleClick() {
  if (collapseMenu.classList.contains("max-lg:hidden")) {
    collapseMenu.classList.remove("max-lg:hidden", "max-lg:opacity-0");
    collapseMenu.classList.add("max-lg:opacity-100");
  } else {
    collapseMenu.classList.add("max-lg:opacity-0");
    collapseMenu.classList.remove("max-lg:opacity-100");
    collapseMenu.addEventListener(
      "transitionend",
      () => collapseMenu.classList.add("max-lg:hidden"),
      { once: true }
    );
  }
}

toggleOpen.addEventListener("click", handleClick);
toggleClose.addEventListener("click", handleClick);

