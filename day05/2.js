import { INPUT } from "./input.js";
const RULES = INPUT.RULES;
const UPDATES = INPUT.UPDATES;

const ruleNums = new Set(RULES.flat());
const relations = {};

// create map skeleton
for (const ruleNum of ruleNums) {
  if (!relations[ruleNum]) relations[ruleNum] = {};
  relations[ruleNum].before = new Set();
  relations[ruleNum].after = new Set();
}

// populate map
for (const rule of RULES) {
  relations[rule[0]].before.add(rule[1]);
  relations[rule[1]].after.add(rule[0]);
}

const isInCorrectOrder = (update) => {
  for (let i = 0; i < update.length; i++) {
    // is there any number before update[i], that shouldn't be there
    for (let j = 0; j < i; j++) {
      if (relations[update[i]].before.has(update[j])) return false;
    }
    // is there any number after update[i], that shouldn't be there
    for (let j = i; j < update.length; j++) {
      if (relations[update[i]].after.has(update[j])) return false;
    }
  }
  return true;
};

const middleValue = (arr) => {
  return arr[(arr.length - 1) / 2];
};

// store all incorrect updates
const incorrectUpdates = [];
for (const update of UPDATES) {
  if (!isInCorrectOrder(update)) {
    incorrectUpdates.push(update);
  }
}

let total = 0;
// order the incorrectly ordered updates
for (const update of incorrectUpdates) {
  update.sort((a, b) => (relations[a].after.has(b) ? -1 : 1));
  total += middleValue(update);
}

console.log(total);
