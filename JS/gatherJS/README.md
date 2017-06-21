# Gather.js
Naive JS implementation of tidyr's `gather` function.
Intended for use with JSON-styled tabular data... like you'd get from `d3.dsv`.

The same function is implemented in several ways: using ECMAScript2015, and then with Ramda.js.

## gather-vanilla
Usage:

``` javascript
const data = [
  {Factor1: 'x1', A: 1, B: 74, C: 0.3},
  {Factor1: 'x2', A: 2, B: 89, C: 0.12},
  {Factor1: 'x3', A: 3, B: 30, C: 0.5}
  ];

const fields = ['A', 'B', 'C'];
const out = gather(data, 'Factor2', 'Value', ...fields);
out.forEach(item => { console.log(item); });
```

...which should produce...

``` javascript
Object {Factor2: "A", Value: 1, Factor1: "x1"}
Object {Factor2: "B", Value: 74, Factor1: "x1"}
Object {Factor2: "C", Value: 0.3, Factor1: "x1"}
Object {Factor2: "A", Value: 2, Factor1: "x2"}
Object {Factor2: "B", Value: 89, Factor1: "x2"}
Object {Factor2: "C", Value: 0.12, Factor1: "x2"}
Object {Factor2: "A", Value: 3, Factor1: "x3"}
Object {Factor2: "B", Value: 30, Factor1: "x3"}
Object {Factor2: "C", Value: 0.5, Factor1: "x3"}
```

Note the spread operator (`...`) in the signature of `gather`. This means that the two lines below are equivalent:

``` javascript
gather(data, 'Factor2', 'Value', ...fields)
gather(data, 'Factor', 'Value', 'A', 'B', 'C')
```

This way, `gather` can be explicitly parameterized for a small number of fields, but we can also dump a larger number of values in. Suppose we have a very wide data set, with 28 columns, `['Factor1', 'Factor2', 'A', 'B', ..., 'Z']`. If we wish to "lengthen" all but the first two columns, 'Factor1' and 'Factor2', we could simply relabel them all under `Factor3` like so:

``` javascript
let columns = Object.keys(d3.values(reallyWideData)[0]);
let theAlphabet = columns.slice(2);
let longData = gather(reallyWideData, 'Factor3', 'Value', ...theAlphabet);
```

## gather-ramda

```javascript
let k = 'Factor2';
let v = 'Value';
let columns = ['A','B', 'C'];
let gatherer = gatherRow(k, v, columns);
```
Now, we could just reduce by concat...
```javascript
let gather = R.compose(R.flatten, R.map(gatherer));
let gathered = gather(data);
```
...or, we can apply gatherRow to an arbitrary stream of rows with most.concatMap!
```javascript
let most = require('most');
let gatheredStream = streamOfWideRows.concatMap(gatherer);
```
