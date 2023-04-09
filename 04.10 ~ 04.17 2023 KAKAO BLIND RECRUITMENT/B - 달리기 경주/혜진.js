function solution(players, callings) {
  const race1 = {}
  const race2 = {}
  players.forEach((name, i) => {
    race1[name] = i
    race2[i] = name
  })

  callings.forEach(name => {
    let idx = race1[name]
    let prevName = race2[idx - 1]
    race1[name] = idx - 1; race1[prevName] = idx
    race2[idx] = prevName; race2[idx - 1] = name
  })
  const ans = []
  for (let i = 0; i < players.length; i++) {
    ans.push(race2[i])
  }
  return ans
}


// function solution(players, callings) {
//   const race = {}
//   players.forEach((name, i) => race[name] = i)
  
//   callings.forEach(name => {
//     let idx = race[name]
//     let prevName = players[idx - 1]
//     players[idx] = prevName
//     players[idx - 1] = name
//     race[name]--
//     race[prevName]++
//   })
  
//   return Object.entries(race).sort((a, b) => a[1] - b[1]).map(v => v[0])
// }
