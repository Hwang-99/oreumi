function getRandomChoice() {
  const choices = ["가위", "바위", "보"];
  const randomIndex = Math.floor(Math.random() * choices.length);
  return choices[randomIndex];
}

console.log(getRandomChoice());
