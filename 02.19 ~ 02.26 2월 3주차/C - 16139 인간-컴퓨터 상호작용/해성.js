const input = () => {
  return require("fs")
    .readFileSync("./input.txt")
    .toString()
    .trim()
    .split("\n");
};
let ob;
const result = [];
const makeSumTable = () => {
  ob = Array(27)
    .fill()
    .map((_) => Array(WORD.length + 1).fill(0));
  for (let i = 0; i < 26; i++)
    for (let j = 0; j < WORD.length; j++)
      ob[i][j] = (ob[i][j - 1] ?? 0) + +(i == WORD[j].charCodeAt() - 97);
};

const solve = (letter, start, end) => {
  //   if (!ob[letter]) {
  //     return 0;
  //   } else {
  //   console.log(letter, start, end);
  if (start == 0) {
    return ob[letter][end];
  }
  return ob[letter][end] - ob[letter][start - 1];
  //   }
};

const INPUT = input();
const WORD = INPUT.shift().trim();
const Q = Number(INPUT.shift().trim());
const wordList = INPUT.map((el) => el.trim());
makeSumTable();
for (let i = 0; i < Q; i++) {
  const pb = wordList[i].split(" ");
  result.push(solve(pb[0].charCodeAt() - 97, Number(pb[1]), Number(pb[2])));
}
console.log(result.join("\n"));

// const I = require("fs")
//   .readFileSync("./input.txt")
//   .toString()
//   .trim()
//   .split("\n");
// const [S, q, O] = [I[0], +I[1], []];
// const l = S.length;
// const A = Array(26)
//   .fill()
//   .map((_) => Array(l).fill(0));
// for (let i = 0; i < 26; i++)
//   for (let j = 0; j < l; j++)
//     A[i][j] = (A[i][j - 1] ?? 0) + +(i == S[j].charCodeAt() - 97);
// // A에 a-z의 누적 합 저장
// console.log(A);
// for (let i = 2; i < q + 2; i++) {
//   const [a, l, r] = I[i].split(" ");
//   const j = a.charCodeAt() - 97;
//   O.push(A[j][r] - (A[j][l - 1] ?? 0));
// }
// // console.log(O.join("\n"));
