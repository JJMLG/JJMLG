const INPUT = require("fs").readFileSync("./input.txt").toString().trim();
// const INPUT = require("fs").readFileSync("/dev/stdin").toString().trim();

const solve = () => {
  const result = INPUT;
  let rev_result = INPUT.split("").reverse().join("");
  if (rev_result == result) {
    return rev_result.length;
  }
  for (let i = 1; i < result.length; i++) {
    let arr = result.split("").slice(i).join("");
    const reverse_arr = result.split("").slice(i).reverse().join("");
    if (arr === reverse_arr) {
      return result.length + i;
    }
  }
};
console.log(solve());
