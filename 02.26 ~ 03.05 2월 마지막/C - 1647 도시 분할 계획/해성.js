const Input = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n");
const [N, M] = Input.shift().split(" ").map(Number);

const COMP = (a, b) => {
  if (a[2] > b[2]) {
    return 1;
  }
  return -1;
};

const parent = new Array(N + 1).fill(0).map((el, idx) => (el = idx));

const findParent = (node) => {
  if (parent[node] == node) return node;
  return (parent[node] = findParent(parent[node]));
};
const union = (first, second) => {
  const firstParent = findParent(first);
  const secondParent = findParent(second);
  if (firstParent < secondParent) {
    parent[secondParent] = firstParent;
  } else parent[firstParent] = secondParent;
};

let result = [];
const graph = Input.map((el) => {
  return el.trim().split(" ").map(Number);
}).sort(COMP);

graph.forEach((el) => {
  const [first, second, value] = el;
  if (findParent(first) != findParent(second)) {
    union(first, second);
    result.push(value);
  }
});
result.pop();
result = result.reduce((sums, val) => {
  return sums + val;
}, 0);

console.log(result);
