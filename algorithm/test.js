const end = 100;
let sum = 0;
for (let i = 1; i < end; i++) {
  if (i % 2 === 0) {
    sum += end;
  }
}
console.log("전체 합은 ${sum}입니다.");
