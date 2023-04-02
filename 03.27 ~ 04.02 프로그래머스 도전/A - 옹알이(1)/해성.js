function solution(babbling) {
  let answer = babbling.filter((el) => {
    let cnt = 4;
    while (cnt--) {
      if (el[0] === "a") {
        el = el.split("aya").join("");
      }
      if (el[0] === "a") {
        el = el.split("aya").join("");
      }
      if (el[0] === "y") {
        el = el.split("ye").join("");
      }
      if (el[0] === "w") {
        el = el.split("woo").join("");
      }
      if (el[0] === "m") {
        el = el.split("ma").join("");
      }
    }
    return el;
  });
  return babbling.length - answer.length;
}
