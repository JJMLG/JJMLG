const INPUT = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n");
const [N, M] = INPUT.map(Number);
const word = INPUT.pop().split("");

let idx = 0;
let letter = "";
let IOIarr = [];
let endIdx = 0;
while (idx < M) {
  if (word[idx] == "I") {
    letter = ["I"];
    endIdx = idx + 1;
    while (endIdx < M) {
      if (letter[letter.length - 1] == "I" && word[endIdx] == "O") {
        letter.push(word[endIdx]);
      } else if (letter[letter.length - 1] == "O" && word[endIdx] == "I") {
        letter.push(word[endIdx]);
      } else {
        break;
      }
      endIdx++;
    }
    idx = endIdx - 1;
    if (letter[letter.length - 1] == "O") letter.pop();
    if (letter.length > 1) {
      IOIarr.push(letter.join(""));
    }
  }
  idx++;
}
let result = 0;
IOIarr.map((el) => {
  const num = (el.length - 1) / 2 - N + 1;
  result += num < 0 ? 0 : num;
});
console.log(result);
