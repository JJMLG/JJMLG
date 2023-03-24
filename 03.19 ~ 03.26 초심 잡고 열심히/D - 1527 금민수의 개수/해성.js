const [A, B] = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .split(" ")
  .map((el) => el.trim());

const maxLen = B.length;
const sets = new Set();

const dfs = (dep, nowWord) => {
  if (dep > maxLen) return;
  if (+nowWord >= +A && +nowWord <= +B) {
    sets.add(nowWord);
  }
  dfs(dep + 1, nowWord + "4");
  dfs(dep + 1, nowWord + "7");
};

dfs(0, "");

console.log(sets.size);
