'use strict';
let R = require('ramda');

// lengthenRow :: String -> String -> [Object]
let lengthenRow = R.curry(function (keyLabel, valueLabel, row) {
  // This point-free thing is kinda cute, but I think the original was clearer.
  // Note: lengthenRow is just the trivial gatherRow when no columns are kept!
  let customKV = key => ({[keyLabel]: key,
                          [valueLabel]: row[key]});
  let customEntries = R.map(customKV);
  let lengthen = R.compose(customEntries, R.keys);
  return lengthen(row);
});

// gatherRow :: String -> String -> [String] -> Object -> [Object]
let gatherRow = R.curry(function (keyLabel, valueLabel, columns, row) {
  // Convert wide JSON representation of CSV row into long format
  let pickWithout = R.pick(R.difference(R.keys(row), columns));
  let pickWith = R.pick(columns);
  let kept = pickWithout(row);
  let wide = pickWith(row);

  let lengthened = lengthenRow(keyLabel, valueLabel, wide);

  let mergeAll = R.map(R.merge(kept));
  return mergeAll(lengthened);
});

module.exports.gatherRow = gatherRow;
