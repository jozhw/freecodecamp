function orbitalPeriod(arr) {
  const GM = 398600.4418;
  const earthRadius = 6367.4447;

  let average = [];
  
  for (let i = 0; i < arr.length; i++) {
    let axis = Math.pow(earthRadius + arr[i]["avgAlt"], 3);
    let sqrt = Math.sqrt(axis/GM);
    let period = Math.round(2 * Math.PI * sqrt)
    average.push({"name": arr[i].name, "orbitalPeriod": period})

  }
  return average

}

orbitalPeriod([{name : "sputnik", avgAlt : 35873.5553}]);