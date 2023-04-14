// function solution(score) {
//   const comp = (a, b) => {
//     return b[1] - a[1];
//   };
//   score = score.map((el, idx) => [idx + 1, (el[0] + el[1]) / 2]);
//   score = score.sort((a, b) => comp(a, b));
//   const record = new Array(score.length + 1).fill(0);
//   let rank = 1;
//   let sameRankCnt = 1;
//   record[score[0][0]] = 1;
//   for (let i = 1; i < score.length; i++) {
//     if (score[i - 1][1] === score[i][1]) {
//       record[score[i][0]] = rank;
//       sameRankCnt++;
//     } else {
//       rank += sameRankCnt;
//       sameRankCnt = 1;
//       record[score[i][0]] = rank;
//     }
//   }
//   record.shift();
//   return record;
// }

function solution(score) {
  return score.map((el) => {
    return score.reduce(
      (init, value) =>
        (init += (value[0] + value[1]) / 2 > (el[0] + el[1]) / 2),
      1
    );
  });
}
