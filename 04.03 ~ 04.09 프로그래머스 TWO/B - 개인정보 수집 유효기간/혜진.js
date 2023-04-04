const makeDateNum = (date) => {
  date = date.split('.')
  // JS에서 string * number => number
  return (date[2] * 1) + (date[1] * 28) + (date[0] * 12 * 28)
}

function solution(today, terms, privacies) {
  today = makeDateNum(today)
  
  const month = new Object()
  terms.forEach(t => {
    t = t.split(' ')
    month[t[0]] = t[1] * 28
  });

  const ans = []
  for (let i = 0; i < privacies.length; i++) {
    const tmp = privacies[i].split(' ')
    const date = makeDateNum(tmp[0]) + month[tmp[1]]
    if (today >= date) ans.push(i + 1)
  }
  return ans
}
