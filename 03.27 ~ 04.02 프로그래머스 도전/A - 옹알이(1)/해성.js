function solution(babbling) {
  let answer = babbling.filter((el) => {
    let cnt = 4;
    while (cnt--) {
      switch (el[0]) {
        case "a":
          el = el.split("aya").join("");
          break;

        case "y":
          el = el.split("ye").join("");
          break;
        case "w":
          el = el.split("woo").join("");
          break;

        default:
          el = el.split("ma").join("");
      }
    }
    return el;
  });
  return babbling.length - answer.length;
}
