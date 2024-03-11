#!/usr/bin/node

const argv = process.argv.slice(2);

const undef = 'undefined';

if (argv[0]) {
  if (argv[1]) {
    console.log(argv[0] + ' is ' + argv[1]);
  } else {
    console.log(argv[0] + ' is ' + undef);
  }
} else {
  console.log(undef + ' is ' + undef);
}
