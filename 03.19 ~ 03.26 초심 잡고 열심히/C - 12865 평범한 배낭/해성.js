const [[N, limit], ...INPUT] = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => {
    return el.split(" ").map(Number);
  });

// const comp = (a, b) => {
//   if (a[0] > b[0]) return 1;
//   return -1;
// };
// INPUT.sort(comp);
// const maxValue = Math.max(...INPUT.map((el) => el[1]));
let max = 0;
let dp = Array.from(Array(N + 1), () => new Array(limit + 1).fill(0));

for (let idx = 1; idx <= N; idx++) {
  for (let j = 1; j <= limit; j++) {
    const W = INPUT[idx - 1][0];
    const V = INPUT[idx - 1][1];
    if (W <= j) {
      dp[idx][j] = Math.max(dp[idx - 1][j], dp[idx - 1][j - W] + V);
    } else {
      dp[idx][j] = dp[idx - 1][j];
    }
  }
}
console.log(dp[N][limit]);

// let visit = new Array(N).fill(0);
// const DFS = (weight, sums) => {
//   if (weight > limit) return;
//   if (sums > max) max = sums;
//   for (let i = 0; i < INPUT.length; i++) {
//     if (visit[i]) continue;
//     visit[i] = 1;
//     DFS(weight + INPUT[i][0], sums + INPUT[i][1]);
//     visit[i] = 0;
//   }
// };
// DFS(0, 0);
