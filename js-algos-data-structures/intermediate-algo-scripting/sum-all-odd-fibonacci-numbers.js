function sumFibs(num) {
  let term = 0;
  let index = 0;
  let array = [];

  while (term < num + 1) {
    array.push(term)
    
    if (term == 0) {
      term = array[term] + 1
    } else {
      term = array[index - 1] + term
    }

    index += 1
  }

  
  return array.filter((number) => {
    return number % 2 != 0
  })
  .reduce((previous, current) => {
   return previous + current
  }, 0)
}

sumFibs(4);

console.log(sumFibs(4))