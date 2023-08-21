function uniteUnique(...arr) {
  let listArgs = [...arr];
  let rawArray = listArgs.reduce((previous, current) => {
    return previous.concat(current)
  }, [])
  let finalArr = [];
  for (let i = 0 ; i < rawArray.length; i++) {
    if (finalArr.includes(rawArray[i])){
      continue
    } else {
      finalArr.push(rawArray[i])
    }
  }



  return finalArr;
}

uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);