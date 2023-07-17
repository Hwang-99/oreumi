// 1. 함수를 선언 (유일하게 hoisting 가능)

// console.log(example);
// var example;

// console.log(add(3, 5));

function add(a, b) {
  return a + b;
}

// let addNumbers = add(3, 5);

// 2. 함수 표현식
// console.log(subtract);
let subtract = function (a, b) {
  return a - b;
};

// 3. 화살표 함수
let subtract2 = (a, b) => {
  return a - b;
};
console.log(subtract2(3, 5));
