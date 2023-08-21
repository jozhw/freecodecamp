function smallestCommons(arr) {
   let [min, max] = arr.sort((a, b) => a - b)

    let array = Array(max - min + 1).fill(0).map((_, number) => number + min);

    // formula to find the greatest common divisor using Euclidean algorithm
    let gcd = (max, min) => {
      return (min == 0) ? max: gcd(min, max % min)
    }

    // formula for least common multiple using Euclidean algo
    let lcm = (max, min) => {
      return max*min/gcd(max,min)
    }

    // find lcm for all of the values
    return array.reduce((accum, current) => {
      return lcm(accum, current);
    }, )


}

smallestCommons([1,5]);
