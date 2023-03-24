const [[n, b, a], presentList] = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .split("\n")
  .map((el) => {
    return el.split(" ").map(Number);
  });
presentList.sort((a, b) => a - b);

let start = -1;
let end = n + 1;
let mid;
while (start + 1 < end) {
  mid = Math.floor((start + end) / 2);
  let sum = 0;
  for (let i = mid - 1; i >= Math.max(0, mid - a); i--) {
    sum += presentList[i] / 2;
    if (sum > b) break;
  }
  for (let i = mid - a - 1; i >= 0; i--) {
    sum += presentList[i];
    if (sum > b) break;
  }
  if (sum <= b) start = mid;
  else end = mid;
}
console.log(start);

// presentList.sort((a, b) => b - a);

// let maxx = 0;
// for (let i = 0; i < presentList.length; i++) {
//   let start = i;
//   let discount = a;
//   let sums = 0;
//   let cnt = 0;
//   while (start < presentList.length) {
//     if (discount) {
//       sums += presentList[start] / 2;
//       cnt++;
//       discount--;
//     } else {
//       sums += presentList[start];
//       cnt++;
//     }
//     if (sums > b) {
//       cnt--;
//       break;
//     }
//     start++;
//   }
//   if (maxx <= cnt) {
//     maxx = cnt;
//   } else {
//     break;
//   }
// }

// console.log(maxx);
