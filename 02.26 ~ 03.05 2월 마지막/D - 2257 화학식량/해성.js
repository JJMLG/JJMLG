const INPUT = require("fs").readFileSync("./input.txt").toString().trim();

const CH = { H: "1", C: "12", O: "16" };

const stack = [];
for (let i = 0; i < INPUT.length; i++) {
  if (INPUT[i] == ")") {
    let sum = 0;
    while (1) {
      const top = stack.pop();
      if (top == "(" || stack.length == 0) {
        stack.push(sum.toString());
        break;
      } else if (top == "C" || top == "O" || top == "H") {
        sum += CH[top];
      } else {
        sum += Number(top);
      }
    }
  } else {
    if (INPUT[i] == "(") stack.push("(");
    else if ("0" <= INPUT[i] && INPUT[i] <= "9") {
      stack.push((stack.pop() * INPUT[i]).toString());
    } else stack.push(CH[INPUT[i]]);
  }
}
const result = stack.reduce((sum, value) => {
  return (sum += Number(value));
}, 0);
console.log(result);
// console.log(INPUT);
// let newArr = INPUT.map((val, idx) => {
//   if (val == "H") {
//     return "+1";
//   } else if (val == "C") {
//     return "+12";
//   } else if (val == "O") {
//     return "+16";
//   }
//   if (idx > 0 && "0" <= val && val <= "9") {
//   }
//   if (idx > 0 && INPUT[idx - 1] == ")") {
//     if ("0" <= val && val <= "9") return `*${val}`;
//     else return;
//   } else return val;
// });
// newArr = newArr.join("");
// console.log(newArr);
