// 1. div 요소를 선택하고 변수 container에 할당하세요.

let container = document.getElementById("container");
//변수명 = 연결한 html문서.id값으로 해당요소를 가져옴("id명")

// 2. Hello, world에 클래스 'boldText'를 추가하세요.

let helloWorld = document.querySelector("a");
helloWorld.classList.add("boldText");
//helloWorld라는 변수에 "boldText"라는 클래스를 추가합니다(add)

// 3. forEach 메서드를 이용해 Item 1, 2, 3의 텍스트 컬러를 파랑색으로 바꾸세요.

let itemList = document.querySelectorAll("li");
// itemList 변수에 "li"인 요소를 모두 추가합니다

itemList.forEach(function (item) {
  item.style.color = "blue";
  // itemList 배열을 돌며 각 요소를 매개변수로 넣고
});

// 4. class가 alert인 모든 요소를 한번에 선택하고 클릭 시에 알림창이 뜨도록 바꾸세요.

let buttonList = document.querySelectorAll(".alert");
buttonList.forEach(function (buttonList) {
  //forEach로 반복하면서 각 요소에 add~로 기능을 추가합니다
  buttonList.addEventListener("click", function () {
    //실행은 언제? click했을때>>function내 내용을 실행합니다
    alert("클릭되었습니다!");
  });
});

// 5. 'This is another paragraph.'를 '이것은 문장입니다'로 바꾸세요.
let paragraphs = document.getElementsByClassName("description");
for (let i = 0; i < paragraphs.length; i++) {
  //innerHTML = 해당 요소 내에 있는 내용
  if (paragraphs[i].innerHTML === "This is another paragraph.") {
    paragraphs[i].innerHTML = "이것은 문장입니다.";
  }
}

// 6. div 내에 <h2>Bye, world!</h2>를 추가하세요.
let heading2 = document.createElement("h2");
heading2.textContent = "Bye, world!";
//요소를 위에서 직접 만들어서 appendChild로 해당 요소를 container내에 추가
container.appendChild(heading2);

// 7. Item 2 요소를 제거하세요.
let item2 = container.querySelector("li:nth-child(2)");
//li의 마지막 요소를 저장해서 remove로 제거
item2.remove();
