async function wakeUp() {
  return console.log("아침에 일어나서 강의듣기!");
}

async function eatLunch() {
  return new Promise((resolve, reject) => {
    setTimeout(function () {
      const data = "점심시간에 점심먹기!";
      resolve(data);
    }, 3000);
  });
}

async function endClass() {
  return console.log("강의가 끝났다! 놀아야지!");
}

async function startDay() {
  wakeUp();
  const data = await eatLunch();
  const end = await endClass();
  const dinner = await eatDinner();
  const sleep = await gotoSleep();
}

startDay();
