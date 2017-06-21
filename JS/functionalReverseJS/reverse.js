function empty(coll) { return 0 === coll.length; }

/**
 * These one-liners are equivalent...
 * But they're hard to read, and both are undefined on empty collections. :(
 */

function reverse([h, ...t]) { return empty(t) ? h : reverse(t).concat(h); }

let reverse = ([h,...t]) => empty(t) ? h : reverse(t).concat(h);

/**
 * Less pretty, but actually works on empty collections.
 */

function reverse(coll) {
  if (empty(coll)) return coll;
  let [h,...t] = coll;
  return empty(t) ? h : reverse(t).concat(h);
}
