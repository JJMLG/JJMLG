const IN = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = IN.shift().split(" ").map(Number);
const K = Number(IN.pop());
const pattern = IN.map((el) => el.trim());
const patternMap = {};

let answer = 0;

const find = (el) => {
  const count = el.split("").reduce((init, val) => {
    return init + !Number(val);
  }, 0);
  return count;
};
const solve = () => {
  pattern.map((el) => {
    if (patternMap[el] && patternMap[el].count != -1) {
      patternMap[el].count++;
      if (answer < patternMap[el].count) answer = patternMap[el].count;
    } else {
      const count = find(el);
      if (count % 2 == K % 2 && count <= K) {
        patternMap[el] = {
          zeroCount: count,
          count: 1,
        };
        if (answer < patternMap[el].count) {
          answer = patternMap[el].count;
        }
      } else {
        patternMap[el] = {
          zeroCount: count,
          count: -1,
        };
      }
    }
  });
};
solve();
console.log(answer);
