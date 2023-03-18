const input = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n");

let answer = 0;
const DFS = (node, dep) => {
  visit[node] = 1;
  let cnt = 0;

  for (let i = 0; i < adjList[node].length; i++) {
    const nextNode = adjList[node][i];
    if (visit[nextNode]) continue;
    cnt++;
    DFS(nextNode, dep + 1);
  }
  if (!cnt) {
    answer += dep;
    return;
  }
};

const N = +input.shift();
const adjList = Array.from(Array(N + 1), () => new Array());
const visit = new Array(N + 1).fill(0);

const Trees = input
  .map((el) => {
    return el.trim().split(" ");
  })
  .map((number) => {
    let [n1, n2] = number;
    n1 = +n1;
    n2 = +n2;

    adjList[n1].push(n2);
    adjList[n2].push(n1);
  });

DFS(1, 0);
console.log(answer % 2 ? "Yes" : "No");
