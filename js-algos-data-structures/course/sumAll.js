function sumAll(arr) {
  // find the max to start the recursion
  let begin = Math.max(...arr);
  // find the min to end the recursion
  let end = Math.min(...arr);
  // define the function for the recursion
  function appUp(begin, end) {
    if (begin == end) {
      return end;
    } else {
      return begin + addUp(begin - 1, end);
    }
  }
  return addUp(begin, end);
}
