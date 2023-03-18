const [[N], ...sche] = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));
sche.sort((a, b) => a[0] - b[0]);

// const IN = require("fs")
//   .readFileSync("./input.txt")
//   .toString()
//   .trim()
//   .split("\n");
// const N = +IN.shift();

// const sche = IN.map((el) => {
//   return el.trim().split(" ").map(Number);
// }).sort((a, b) => a[0] - b[0]);

const solve = () => {
  let day = 0;
  let addDay = 0;
  for (let i = 0; i < sche.length; i++) {
    let [di, ti] = sche[i];

    let limitDay = di - Math.floor(di / 7) * 2;

    if (di % 7 == 6) limitDay--;

    day += ti;

    if (day > limitDay) {
      addDay += day - limitDay;
      day = limitDay;
    }
    if (addDay > di) return -1;
  }
  return addDay;
};
const answer = solve();
console.log(answer);

// const [[n], ...tasks] = (require("fs").readFileSync("./input.txt") + "")
//   .trim()
//   .split("\n")
//   .map((v) => v.split(" ").map(Number));

// const getSt = (d) => Math.floor(d / 7) * 5 + (d % 7 === 6 ? 5 : d % 7);
// tasks.sort((a, b) => a[0] - b[0]);
// let totalSt = 0;
// let exWork = 0;
// for (const task of tasks) {
//   let [d, t] = task;
//   if (t > getSt(d) - totalSt) {
//     exWork += t - getSt(d) + totalSt;
//     totalSt = getSt(d);
//   } else {
//     totalSt += t;
//   }
//   if (exWork > d) {
//     exWork = -1;
//     break;
//   }
// }
// console.log(exWork);
