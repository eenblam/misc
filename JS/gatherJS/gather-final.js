'use strict';
let R = require('ramda');

// lengthenRow :: String -> String -> [Object]
let lengthenRow = R.curry(function (keyLabel, valueLabel, row) {
  let customKV = key => ({[keyLabel]: key,
                          [valueLabel]: row[key]});
  return Object.keys(row).map(customKV);
});

// gatherRow :: String -> String -> [String] -> Object -> [Object]
let gatherRow = R.curry(function (keyLabel, valueLabel, columns, row) {
  // Convert wide JSON representation of CSV row into an array long format rows
  let pickWithout = R.pick(R.difference(R.keys(row), columns));
  let pickWith = R.pick(columns);
  let kept = pickWithout(row);
  let wide = pickWith(row);

  let lengthened = lengthenRow(keyLabel, valueLabel, wide);

  let mergeAll = R.map(R.merge(kept));
  return mergeAll(lengthened);
});

module.exports.gatherRow = gatherRow;
