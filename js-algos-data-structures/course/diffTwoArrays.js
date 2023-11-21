function diffArray(arr1, arr2) {
  /* to solve the problem of an array as the standard not having an item in the
   * test array, use a dictionary with all fo the values and add the value if
   * present. Then find the keys with value equal to 1 and create a new array
   * out of that
   */

  let arr = [...arr1, ...arr2];

  const dict = Object.assign({}, ...arr.map((x) => ({ [x]: 0 })));

  for (let i = 0; i < arr.length; i++) {
    if (dict.hasOwnProperty(arr[i])) {
      dict[arr[i]] += 1;
    }
  }
  const newArr = [];
  for (let [key, value] of Object.entries(dict)) {
    if (value == 1) {
      if (!!(parseFloat(key) == false)) {
        newArr.push(key);
      } else {
        newArr.push(parseFloat(key));
      }
    }
  }
  return newArr;
}
