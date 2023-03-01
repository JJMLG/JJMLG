const INPUT = require("fs").readFileSync("./input.txt").toString().split("\n");
const N = INPUT.shift();
const storeName = INPUT.shift().trim();
let answer = 0;
const check = (k, candidate) => {
  for (let len = 1; len <= candidate.length - k; len++) {
    let count = 1;
    while (count < storeName.length) {
      if (storeName[count] == candidate[k + len * count]) {
        count++;
      } else break;
    }
    if (count == storeName.length) {
      return 1;
    }
  }
  return 0;
};
const newArr = INPUT.map((candidate, idx) => {
  candidate.trim();
  for (let i = 0; i < candidate.length; i++) {
    if (candidate[i] == storeName[0]) {
      const ret = check(i, candidate);
      if (ret) {
        // console.log(i, candidate);
        answer++;
        break;
      }
    }
  }
});
console.log(answer);
