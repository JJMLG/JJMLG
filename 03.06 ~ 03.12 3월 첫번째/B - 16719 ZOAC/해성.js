const Input = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("");

const visit = new Array(Input.length).fill(0);
const solve = (start, end) => {
  if (start == end) return;
  const minLetter = Input.slice(start, end).sort()[0];
  const minIdx = Input.slice(start, end).indexOf(minLetter) + start;
  visit[minIdx] = 1;

  let word = "";
  for (let i = 0; i < visit.length; i++) {
    if (visit[i]) {
      word += Input[i];
    }
  }
  console.log(word);
  solve(minIdx + 1, end);
  solve(start, minIdx);
};

solve(0, Input.length);
