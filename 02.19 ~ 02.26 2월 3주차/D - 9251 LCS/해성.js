const LCS = () => {
  for (let i = 1; i <= lenB; i++) {
    for (let k = 1; k <= lenA; k++) {
      if (B[i - 1] == A[k - 1]) {
        adjArr[i][k] = adjArr[i - 1][k - 1] + 1;
      } else {
        adjArr[i][k] = Math.max(adjArr[i - 1][k], adjArr[i][k - 1]);
      }
    }
  }
  console.log(adjArr[lenB][lenA]);
};

const [A, B] = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .split("\n")
  .map((el) => el.trim());

const lenA = A.length;
const lenB = B.length;

const adjArr = Array.from(Array(2000), () => Array().fill());
for (let i = 0; i <= lenB; i++) {
  for (let j = 0; j <= lenA; j++) {
    adjArr[i][j] = 0;
  }
}
LCS();
// console.log(adjArr);
// const find = (len) => {
//   //   console.log(end, len);
//   for (let i = 0; i <= end - len; i++) {
//     const templen = 0;
//     for (let k = i; k < i + len; k++) {
//       //   if (A[k] == B[k]) templen++;
//       //   else break;
//     }
//     // if (templen == len) return len;
//   }
//   return 0;
// };
// const solve = (start, mid, end) => {
//   let maxx = 0;
//   while (start <= end) {
//     mid = Number(start + end / 2);
//     const ret = find(mid);
//     if (ret) {
//       start = mid + 1;
//       if (maxx < mid) maxx = mid;
//     } else {
//       end = mid - 1;
//     }
//   }
//   return maxx;
// };
//TODO
//먼저 하나라도 겹치는게 있는지 체크해서 없으면 0 바로 출력
//하나라도 있으면
//최대길이 이분탐색
// 길이 최부터 A,b 중에 작은 길이까지
//최소2라도 되면 바로 2출력 아니면, 2길이씩 -> 하고  총길이 맥시멈까지
// let maxlen;
// let start = 0,
//   mid,
//   end = (maxlen = lenA > lenB ? lenB : lenA);
