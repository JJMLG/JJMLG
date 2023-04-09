const checkBTree = (b_str, start, end) => {
  const root = Math.floor((start + end) / 2);
  const left_c = Math.floor((start + root - 1) / 2);
  const right_c = Math.floor((root + 1 + end) / 2);

  if (start == end) {
    return true;
  }

  if (
    b_str[root] === "0" &&
    (b_str[left_c] === "1" || b_str[right_c] === "1")
  ) {
    return false;
  }

  if (!checkBTree(b_str, start, root - 1)) return false;
  if (!checkBTree(b_str, root + 1, end)) return false;
  return true;
};

// 높이가 h인 이진트리 노드 개수(n) 2**h -1
//n개의 노드를 가진 이진 트리 높이 log2(n+1);
//h= log2(n+1)
function solution(numbers) {
  const answer = numbers.map((number) => {
    let bi_num = number.toString(2);
    let dep = Math.ceil(Math.log2(bi_num.length + 1));
    let nodeCnt = 2 ** dep - 1;
    const bi_tree = bi_num.padStart(nodeCnt, "0");
    return +checkBTree(bi_tree, 0, bi_tree.length - 1);
  });
  return answer;
}

// b안.
// function ceilLog2(n) {
//   return Math.ceil(Math.log2(n));
// }
// function possible(btree) {
//   if (btree.length <= 1) return true;
//   const mid = btree.length >> 1;
//   const sub = [btree.slice(0, mid), btree.slice(mid + 1)];
//   if (btree[mid] == "1") return sub.every(possible);
//   else return sub.every((btree) => !+btree);
// }

// function makeBinaryTree(n) {
//   const dep = ceilLog2(n.length + 1);
//   const nodeCnt = 2 ** dep - 1;

//   const btree = n.padStart(nodeCnt, "0");
//   return btree;
// }

// function solution(numbers) {
//   return numbers
//     .map((number) => number.toString(2))
//     .map(makeBinaryTree)
//     .map(possible)
//     .map(Number);
// }
