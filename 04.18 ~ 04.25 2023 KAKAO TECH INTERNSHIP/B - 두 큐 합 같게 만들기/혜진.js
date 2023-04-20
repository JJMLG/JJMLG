// // 시간초과 (파이썬은 통과됨)
// function f(bQ, sQ, bS, sS) {
//   v = bQ.shift()
//   sQ.push(v)
//   return [bS - v, sS + v]
// }

// function solution(queue1, queue2) {
//   let s1 = queue1.reduce((acc, cur) => acc + cur)
//   let s2 = queue2.reduce((acc, cur) => acc + cur)
//   if ((s1 + s2) % 2) return -1

//   let cnt = queue1.length * 3
//   let ans = 0
//   while (cnt--) {
//     if (s1 === s2) return ans
//     if (s1 > s2) [s1, s2] = f(queue1, queue2, s1, s2)
//     else [s2, s1] = f(queue2, queue1, s2, s1)
//     ans++
//   }
//   return -1
// }


function solution(queue1, queue2) {
  let s1 = queue1.reduce((acc, cur) => acc + cur, 0)
  let s2 = queue2.reduce((acc, cur) => acc + cur, 0)
  if ((s1 + s2) % 2) return -1        // 합이 홀수면 반으로 나눌 수 없음

  const target = (s1 + s2) / 2
  const Q = [...queue1, ...queue2]    // 큐를 합쳐야 함
  let i = 0                           // 왼쪽 큐의 시작 인덱스
  let j = queue1.length               // 오른쪽 큐의 시작 인덱스

  for (let cnt = 0; cnt < queue1.length * 3; cnt++) {
    if (s1 === target) return cnt
    if (s1 > target) s1 -= Q[i++]
    else s1 += Q[j++]
  }
  return -1
}

console.log(solution([3, 2, 7, 2], [4, 6, 5, 1]))   // 2
console.log(solution([1, 2, 1, 2], [1, 10, 1, 2]))  // 7
console.log(solution([1, 1], [1, 5]))               // -1
