function steamrollArray(arr) {
  return arr.reduce((accum, current) => {
    if (Array.isArray(current) == true) {
      // recursive function to break down the array
      return accum.concat(steamrollArray(current))
    } else {
      // concat once array is proken down
      return accum.concat(current)
    }

  }, [])
}

steamrollArray([1, [2], [3, [[4]]]]);