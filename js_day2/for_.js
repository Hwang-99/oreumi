// const fruits = ["사과", "바나나", "수박"];

// for (const fruit in fruits) {
//   console.log(fruit, typeof fruit, fruits[fruit])
// };

// const fruits = ["사과", "바나나", "수박"];

// for (const fruit of fruits) {
//   console.log(fruit, typeof fruit, fruits[fruit]);
// }

// const fruits = ["사과", "바나나", "수박"];

// fruits.forEach((fruit, index) => {
//   console.log(fruit, typeof fruit, index);
// });

// const numbers = [1, 2, 3, 4, 5];

// const square = numbers.map((numbers) => {
//   return numbers ** 2;
// });

// console.log(square);

// const numbers = [1, 2, 3, 4, 5];

// const sum = numbers.reduce((accumulator, number) => {
//   return accumulator + number;
// }, 0); // 0은 accumulator의 초기값

// console.log(sum);

const numbers = [1, 2, 4, 5, 10];

const even = numbers.filter((number) => {
  if (number % 2 == 0) {
    return true;
  }
  return number % 2 == 0;
});

console.log(even);
