let buttonRemove = document.querySelector("button");
let clickCount = 0;
buttonRemove.addEventListener("click", function () {
  clickCount += 1;
  if (clickCount === 3) {
    buttonRemove.remove();
  }
});
