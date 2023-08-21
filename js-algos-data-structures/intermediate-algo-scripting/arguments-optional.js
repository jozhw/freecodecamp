function addTogether(...args) {
  let argList = [...args];

  for (let i = 0; i < argList.length; i++) {
    if (typeof argList[i] !="number") {
      return undefined;
    }
  }
  if ([...args].length == 2) {
    return [...args].reduce((accum, current) => {
      return accum + current
  }, 0)

  } else if ([...args].length == 1) {
    return function (b) {
      if (typeof b != "number") {
        return undefined
      }
      return parseFloat(args) + b
    }
  }

  
 
}

addTogether(2,3);