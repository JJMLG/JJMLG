const INPUT = require("fs").readFileSync("./input.txt").toString().trim();
let answer;
let word = "";
const NUM = [];
const OPE = INPUT.split("").filter((val, idx) => {
  if (val == "+" || val == "-") {
    if (word != "") {
      const newel = Number(word);
      word = "";
      NUM.push(newel);
      //   return newel;
      return val;
    }
  } else {
    word += val;
  }
});

if (word != "") NUM.push(Number(word));

let sum = NUM.shift();
let startIdx = 0;
let tempSum = 0;
while (startIdx < NUM.length) {
  if (OPE[startIdx] == "+") {
    tempSum += NUM[startIdx++];
  } else {
    sum += tempSum;
    tempSum = NUM[startIdx++];
    while (OPE[startIdx] != "-" && startIdx < OPE.length) {
      tempSum += NUM[startIdx++];
    }
    sum -= tempSum;
    tempSum = 0;
  }
}
if (tempSum) {
  if (OPE.pop() == "-") {
    sum -= tempSum;
  } else {
    sum += tempSum;
  }
}
console.log(sum);
// ++ // 마지막 + 이면 +temppsum
// + - //마지막 -이면 -tempsum
//   --
// -+
// if (tempSum) {

// }

// for (let i = 0; i < NUM.length; i++) {}

// console.log(OPE, NUM);
