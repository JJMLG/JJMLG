const isBannedId = (bString, uString) => {  // 제재 아이디인가? true or false
  if (bString.length !== uString.length) return false
  for (let j = 0; j < bString.length; j++) {
      if (bString[j] !== '*' && bString[j] !== uString[j]) return false
  }
  return true
}

function solution(user_id, banned_id) {
  // 제재 아이디들의 used_id에서의 idx를 문자열로 만들어서 ans에 추가
  let ans = new Set()

  const used = new Array(user_id.length).fill(0)

  const recur = (idxs, bIdx) => {
    if (bIdx === banned_id.length) {
      let tmp = [...idxs].sort()            // 배열로 바꿔서 정렬하고
      ans.add(tmp.join(''))                 // 문자열로 바꿔서 set에 넣으면 중복 제거
      return
    }

    for (let i = 0; i < user_id.length; i++) {
      if (used[i] > 0) continue             // 이미 제재된 아이디면 continue
      if (isBannedId(banned_id[bIdx], user_id[i])) {
        used[i] = bIdx + 1                  // 몇 번째인지 보기 편하려고 1이 아닌 bIdx + 1 사용
        console.log(used)                // 디버깅
        recur(idxs + String(i), bIdx + 1)
        used[i] = 0
      }
    }
  }

  recur('', 0)
  return ans.size
}

const user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
const banned_id = ["*rodo", "*rodo", "******"]
solution(user_id, banned_id)
