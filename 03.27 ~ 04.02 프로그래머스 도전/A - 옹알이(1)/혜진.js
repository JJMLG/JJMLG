function solution(babbling) {
  const words = ['aya', 'ye', 'woo', 'ma']
  
  const arr = [...words]                              // 옹알이 할 수 있는 모든 경우를 담을 예정
  const used = [0, 0, 0, 0]
  
  const recur = (cur, end, word) => {
    if (cur === end) {
      arr.push(word)
      return
    }
    for (let i = 0; i < 4; i++) {
      if (used[i]) continue
      used[i] = 1
      recur(cur + 1, end, word + words[i])
      used[i] = 0
    }
  }
  
  words.forEach((v, i) => {                           // 시작 단어가 v
    used[i] = 1
    for (let e = 2; e < 5; e++) recur(1, e, v)        // 1개짜리는 담겨있고, 2개부터 4개까지
    used[i] = 0
  })
  
  babbling = babbling.filter(v => arr.includes(v))    // arr에 있는것만 남기기
  return babbling.length
}
