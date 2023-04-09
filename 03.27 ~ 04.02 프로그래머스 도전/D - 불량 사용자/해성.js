const visit = [0, 0, 0, 0];
const result = [0, 0, 0];
const dfs = (dep) => {
  if (dep == 3) {
    // console.log(visit);
    console.log(result);
    return;
  }

  for (let i = 1; i <= 3; i++) {
    if (visit[i]) continue;
    visit[i] = 1;
    result[dep] = i;
    dfs(dep + 1);
    visit[i] = 0;
    result[dep] = 0;
  }
};

dfs(0);
// const comb = [];
// let visit;
// let ban;
// let user;
// const isSame = (a, b) => {
//   if (a.length !== b.length) return 0;
//   for (let i = 0; i < a.length; i++) {
//     if (a[i] !== "*" && a[i] !== b[i]) return 0;
//   }
//   return 1;
// };
// const makeComb = (start, dep, totalDep, tempcomb) => {
//   if (start == dep) {
//     comb.push(tempcomb);
//     return;
//   }
//   for (let i = 0; i < totalDep; i++) {
//     if (visit[i]) continue;
//     if (isSame(ban[start], user[i]) === 0) continue;
//     visit[i] = 1;
//     makeComb(start + 1, dep, totalDep, tempcomb + i);
//     visit[i] = 0;
//   }
// };
// function solution(user_id, banned_id) {
//   ban = banned_id;
//   user = user_id;
//   visit = new Array(banned_id.length).fill(0);
//   makeComb(0, banned_id.length, user_id.length, "");
//   let answer = new Set();

//   let re = comb
//     .map((el) => el.split("").map(Number).sort())
//     .map((el) => answer.add(el.join("")));

//   return answer.size;
// }
