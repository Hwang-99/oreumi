// function Person(name, age) {
//   this.name = name;
//   this.age = age;

//   this.sayHello = function () {
//     console.log(`안녕하세요 ! 제 이름은 ${name}, 나이는 ${age}입니다.`);
//   };
// }

// const Human = new Person("황찬혁", 25); // new = init

// Human.sayHello();

// let number = Number("1");
// console.log(typeof number);

// class Person {
//   constructor(name, age) {
//     this.name = name;
//     this.age = age;
//   }

//   sayHello() {
//     console.log(`안녕하세요 ! 제 이름은 ${this.name}, 나이는 ${this.age}입니다.`);
//   }
// }

//  Human = new Person("황찬혁", 25); // new = init

// Human.sayHello();

let Rectangle = class {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  get area() {
    return this.calcArea();
  }

  calcArea() {}
};
