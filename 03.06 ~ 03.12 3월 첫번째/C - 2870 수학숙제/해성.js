const Input = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .split("\n")
  .map((el) => el.trim());
const N = Input.shift();
const result = [];
Input.map((el) => {
  let idx = 0;
  let words = "";
  while (idx < el.length) {
    if ("0" <= el[idx] && el[idx] <= "9") {
      words += el[idx];
    } else {
      if (words.length) {
        result.push(words);
        words = "";
      }
    }
    idx++;
  }
  if (words.length) result.push(words);
});
console.log(
  result
    .sort((a, b) => a - b)
    //최대 100글자이기때문에 Number로 형변환하면 지수 표기법으로 표현됨
    .map(BigInt)
    .join("\n")
);
