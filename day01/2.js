import { list1, list2 } from "./input.js";

list1.sort();
list2.sort();

let similarityScore = 0;

for (let i = 0; i < list1.length; i++) {
  similarityScore +=
    list1[i] *
    list2.reduce((acc, cur) => {
      return cur === list1[i] ? acc + 1 : acc;
    }, 0);
}

console.log(similarityScore);
