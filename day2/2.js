import { reports } from "./input.js";

const compareLevels = (a, b, order) => {
  if (a > b !== order || a === b) return false;
  if (Math.abs(a - b) > 3) return false;
  return true;
};

const tryEverySplice = (report) => {
  const spliceCombos = [];
  for (let i = 0; i < report.length; i++) {
    const tmp = [...report];
    tmp.splice(i, 1);
    spliceCombos.push(tmp);
  }

  return spliceCombos.some((combo) => isSafe(combo, true));
};

const isSafe = (report, usedDampener = false) => {
  let order = report[0] > report[1];

  for (let i = 1; i < report.length; i++) {
    const a = report[i - 1];
    const b = report[i];

    if (!compareLevels(a, b, order)) {
      if (usedDampener) return false;

      return tryEverySplice(report);
    }
  }
  return true;
};

const safeCount = reports.reduce((acc, cur) => {
  return acc + isSafe(cur);
}, 0);

console.log(safeCount);
