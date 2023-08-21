function sumPrimes(num) {
  let array = [];
  for (let i = 0; i < num + 1; i++){
    array.push(i)
  };

  let divisble = array.slice(2,)

  return array.reduce((previous, current) => {
   if (divisble.some((denom) => {
      if (denom != current){
          return current % denom == 0
      }
    }) || current == 1) {
      return previous
    } else {
      return previous + current;
    }
  }, 0)

}

sumPrimes(10);
