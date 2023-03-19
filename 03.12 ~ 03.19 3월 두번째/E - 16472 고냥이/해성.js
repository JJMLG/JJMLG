const { start } = require("repl");

let [N, WORD] = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .split("\n")
  .map((el) => el.trim());

N = +N;
const maps = new Map();
const wordList = WORD.split("");
let front = 0;
let rear = 0;
let cnt = 0;
let maxx = 0;
while (front < wordList.length) {
  const res = maps.has(wordList[front]);
  // 만약에 맵에 없다면 그대로 추가
  if (!res) {
    maps.set(wordList[front], 1);
    cnt++;
    //혹시 N보다 크다면 N개 맞춰주기
    while (maps.size > N) {
      const rearcnt = maps.get(wordList[rear]);
      maps.set(wordList[rear], rearcnt - 1);
      cnt--;
      if (rearcnt - 1 == 0) {
        maps.delete(wordList[rear]);
      }
      rear++;
    }
  }
  // 있다면 숫자만 카운트하기
  else {
    maps.set(wordList[front], maps.get(wordList[front]) + 1);
    cnt++;
  }
  front++;
  if (cnt > maxx) maxx = cnt;
}
console.log(maxx);
