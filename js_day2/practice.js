// 1. div 요소를 선택하고 변수 container에 할당하세요.
let container = document.getElementById("container");

// 2. Hello, world에 클래스 'boldText'를 추가하세요.
let helloWorld = document.querySelector("a");
helloWorld.classList.add("boldText");

// 3. forEach 메서드를 이용해 Item 1, 2, 3의 텍스트 컬러를 파랑색으로 바꾸세요.
let itemList = document.querySelectorAll("li");
itemList.forEach(function (item) {
  item.style.color = "blue";
});

// 4. class가 alert인 모든 요소를 한번에 선택하고 클릭 시에 알림창이 뜨도록 바꾸세요.
let buttonList = document.querySelectorAll(".alert");
buttonList.forEach(function (buttonList) {
  buttonList.addEventListener("click", function () {
    alert("클릭되었습니다!");
  });
});

// 5. 'This is another paragraph.'를 '이것은 문장입니다'로 바꾸세요.
let paragraphs = document.getElementsByClassName("description");
for (let i = 0; i < paragraphs.length; i++) {
  if (paragraphs[i].innerHTML === "This is another paragraph.") {
    paragraphs[i].innerHTML = "이것은 문장입니다.";
  }
}

// 6. div 내에 <h2>Bye, world!</h2>를 추가하세요.
let heading2 = document.createElement("h2");
heading2.textContent = "Bye, world!";
container.appendChild(heading2);

// 7. Item 2 요소를 제거하세요.
let item2 = container.querySelector("li:nth-child(2)");
item2.remove();
