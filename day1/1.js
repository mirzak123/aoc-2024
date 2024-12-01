import { list1, list2 } from "./input.js";

list1.sort();
list2.sort();

let sum = 0;
for (let i = 0; i < list1.length; i++) {
  sum += Math.abs(list1[i] - list2[i]);
}

console.log(sum);
