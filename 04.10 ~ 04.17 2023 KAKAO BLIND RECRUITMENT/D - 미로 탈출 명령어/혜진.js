// const dr = [1, 0, 0, -1]
// const dc = [0, -1, 1, 0]

// function solution(n, m, x, y, r, c, k) {
//   const dist = Math.abs(x - r) + Math.abs(y - c)
//   let more = k - dist
//   if (k < dist || more % 2) return 'impossible'

//   let ans = 'z'
//   const dfs = (r, c, cnt, route, N, M, R, C, k) => {
//     if (cnt + Math.abs(r - R) + Math.abs(c - C) > k) return

//     if (r === R && c === C && cnt === k) {
//       ans = route
//       return
//     }

//     for (let d = 0; d < 4; d++) {
//       let nr = r + dr[d]; let nc = c + dc[d];
//       if (nr < 1 || nc < 1 || nr > N || nc > M) continue
//       if (ans > route) dfs(nr, nc, cnt + 1, route + 'dlru'[d], N, M, R, C, k)
//     }
//   }
//   dfs(x, y, 0, '', n, m, r, c, k)
//   return ans
// }



function solution(n, m, x, y, r, c, k) {
  const dist = Math.abs(x - r) + Math.abs(y - c)
  let more = k - dist
  if (k < dist || more % 2) return 'impossible'

  let dCnt = 0; let uCnt = 0; let lCnt = 0; let rCnt = 0;
  if (x < r) dCnt = r - x
  else uCnt = x - r
  if (y < c) rCnt = c - y
  else lCnt = y - c

  let tmp = n - Math.max(x, r)
  const dMore = Math.min(tmp, more/2)
  more -= (dMore * 2)

  tmp = Math.min(y, c) - 1
  const lMore = Math.min(tmp, more/2)
  more -= (lMore * 2)

  const dStr = 'd'.repeat(dCnt + dMore)
  const lStr = 'l'.repeat(lCnt + lMore)
  const rl = 'rl'.repeat(more/2)
  const rStr = 'r'.repeat(rCnt + lMore)
  const uStr = 'u'.repeat(uCnt + dMore)

  return dStr + lStr + rl + rStr + uStr
}


console.log(solution(3, 4, 2, 3, 3, 1, 5))     // dllrl
console.log(solution(2, 2, 1, 1, 2, 2, 2))     // dr
console.log(solution(3, 3, 1, 2, 3, 3, 4))     // impossible
