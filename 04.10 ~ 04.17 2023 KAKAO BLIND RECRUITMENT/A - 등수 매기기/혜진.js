// function solution(score) {
//   const tot = score.map(arr => arr[0] + arr[1])
//   tot.sort((a, b) => b - a)
//   const rank = {}
//   tot.forEach((v, i) => {
//     if ((typeof rank[v]) === 'number') return
//     rank[v] = i + 1
//   })
//   return score.map(arr => rank[arr[0] + arr[1]])
// }


function solution(score) {
  const sum = score.map(arr => arr[0] + arr[1])
  const sorted = sum.slice().sort((a, b) => b - a)
  return sum.map(v => sorted.indexOf(v) + 1)
}
