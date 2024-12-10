import { reports } from "./input.js";

const isSafe = (report) => {
  let order = report[0] > report[1];
  for (let i = 1; i < report.length; i++) {
    const a = report[i - 1];
    const b = report[i];
    if (a > b !== order || a === b) return false;
    if (Math.abs(a - b) > 3) return false;
  }
  return true;
};

const safeCount = reports.reduce((acc, cur) => {
  return acc + isSafe(cur);
}, 0);

console.log(safeCount);
