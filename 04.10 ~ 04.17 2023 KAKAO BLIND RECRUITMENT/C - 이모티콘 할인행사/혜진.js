  // 할인하는 모든 경우의 수를 구한다
const discount = []
const recur = (arr, cur, dep) => {
  if (cur === dep) {
    discount.push([...arr])
    return
  }
  [10, 20, 30, 40].forEach(v => {
    arr[cur] = v
    recur(arr, cur + 1, dep)
  })
}

function solution(users, emoticons) {
  const emoL = emoticons.length
  let ans = [0, 0]
  recur(new Array(emoL).fill(0), 0, emoL)
  // console.log(discount.length)
  
  // 경우의 수를 하나씩 꺼내서
  discount.forEach(discountArr => {
    // 그 경우의 수에 대한 가입자수와 비용을 구한다
    const tmp = [0, 0]
    // 사용자가 모든 이모티콘을 기준에 맞게 구매한다
    users.forEach(([userDiscount, userMoney]) => {
      let cost = 0
      for (let e = 0; e < emoL; e++) {
        if (userDiscount <= discountArr[e]) {
          cost += emoticons[e] * (100 - discountArr[e]) / 100
        }
      }
      // 구매하는데 드는 예상 비용이 사용자의 예산보다 많으면 서비스에 가입하고
      if (cost >= userMoney) tmp[0] += 1
      // 아니면 비용을 지불한다
      else tmp[1] += cost
    })
    
    // 목표에 맞으면 업데이트
    if (tmp[0] > ans[0] || (tmp[0] === ans[0] && tmp[1] > ans[1])) {
      ans = [...tmp]
    }
  })
  return ans
}

console.log(solution([[40, 10000], [25, 10000]], [7000, 9000]))
// [1, 5400]
console.log(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
// [4, 13860]
