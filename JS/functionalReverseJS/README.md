Here's a different implementation, building on the one [here](https://drboolean.gitbooks.io/mostly-adequate-guide/content/ch5.html#functional-husbandry):

```javascript
function reverse (arr) {
  return arr.reduce((acc, x) => [x].concat(acc), []);
}
```

This is a nice and non-recursive solution for arrays, but `reduce` isn't a method of `Str`!

Even if we extended the prototype of `Str`, we would need a different implementation of this `reverse` function in order to pass an empty string, `""`, instead of `[]` as `initialValue`.

And, type safety aside, if our function can't reverse strings, why not just call `arr.reverse()`?
