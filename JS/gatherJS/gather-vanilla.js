'use strict';

function withFields(record, fields) {
  // Returns record with only properties specified in fields
  return fields.reduce((acc, key) =>
    {acc[key] = record[key]; return acc;}, {});
}

function splitRecord(record, ...fields) {
  let withGivenFields = withFields(record, fields);
  let otherFields = Object.keys(record)
    .filter(key => !(fields.includes(key)));
  let withOtherFields = withFields(record, otherFields);
  return [withOtherFields, withGivenFields];
}

function gather(data, keyLabel, valueLabel, ...columns) {
  // Convert wide JSON representation of CSV into long format
  let lengthen = record => Object.keys(record)
    .map(key => ({[keyLabel]: key,
                [valueLabel]: record[key]}));

  return data.map(record => {
    let [keptFields, wideFields] = splitRecord(record, ...columns);
    let longFields = lengthen(wideFields);
    let nestedArrays = longFields.map(
      longField => Object.assign({}, longField, keptFields)
    );
    return nestedArrays;
  }).reduce((acc, arr) => acc.concat(arr), []);
}

module.exports.gather = gather;
