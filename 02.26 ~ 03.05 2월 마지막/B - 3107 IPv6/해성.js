let Input = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split(":");

let newArr = new Array(8).fill("0000");

const start = Input.findIndex((el) => el == "");

Input = Input.filter((el) => (el == "" ? false : true));
const end = 7 - (Input.length - start);

newArr = newArr.map((el, idx) => {
  // console.log(el);
  if (idx < start || idx > end) {
    let word = Input.shift();
    word = word.split("");
    while (word.length < 4) {
      word.unshift("0");
    }
    return word.join("");
  } else return el;
});

newArr = newArr.join(":");
console.log(newArr);
