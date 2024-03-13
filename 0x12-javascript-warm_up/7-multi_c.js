#!/usr/bin/node
if ((isNaN(process.argv[2])) || (process.argv[2] === undefined)) {
  console.log('Missing number of occurrences');
} else {
  let i = parseInt(process.argv[2]);
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
