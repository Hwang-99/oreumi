let decreaseBtn = document.getElementById("decreaseBtn");
let resetBtn = document.getElementById("resetBtn");
let increaseBtn = document.getElementById("increaseBtn");
let countDisplay = document.getElementById("countDisplay");
let progressBar = document.getElementById("progressBar");
let count = 0;

decreaseBtn.addEventListener("click", function () {
  count -= 1;
  countDisplay.innerText = count;
});

resetBtn.addEventListener("click", function () {
  count = 0;
  countDisplay.innerText = count;
});

increaseBtn.addEventListener("click", function () {
  count += 1;
  countDisplay.innerText = count;
});

increaseBtn.onclick = function () {
  progressBar.style.width = "10%";
};

resetBtnBtn.onclick = function () {
  progressBar.style.width = "0";
};

decreaseBtn.onclick = function () {
  progressBar.style.width = "-10%";
};
