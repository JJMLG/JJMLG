function solution(survey, choices) {
  const obj = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 }
  let k, v
  for (let i = 0; i < survey.length; i++) {
    // 뭐가 (4는 어차피 0 더해주니까 k가 뭐든 상관없음)
    k = choices[i] < 4 ? survey[i][0] : survey[i][1]
    // 몇 점인지
    v = Math.abs(choices[i] - 4)
    obj[k] += v
  }
  let ans = ''
  // 만약 같으면 알파벳순이니까 뒤에꺼가 되도록 등호는 뺌
  ans += obj['T'] > obj['R'] ? 'T' : 'R'
  ans += obj['F'] > obj['C'] ? 'F' : 'C'
  ans += obj['M'] > obj['J'] ? 'M' : 'J'
  ans += obj['N'] > obj['A'] ? 'N' : 'A'
  return ans
}