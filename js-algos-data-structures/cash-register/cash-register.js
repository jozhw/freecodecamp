function checkCashRegister(price, cash, cid) {
  let change = {};
  let changedValues = [];
  let changedValuesDic = {};
  let dic = {};
 
  let currencyValues = {
    0.01: "PENNY",
    0.05: "NICKEL",
    0.1: "DIME",
    0.25: "QUARTER",
    1:  "ONE",
    5:  "FIVE",
    10: "TEN",
    20: "TWENTY",
    100: 'ONE HUNDRED'
  }

  // get keys and in reverse order
  let currency = Object.keys(currencyValues).map((value) => {
    return parseFloat(value);
  }).sort((a,b) => {
    return a == b ? 0 : a < b ? 1 : -1
  });
 
  // create object for the cash register values
  for (let i = 0; i < cid.length; i++){
    dic[cid[i][0]] = cid[i][1];
  }

  // change that needs to be given
  let remainder = cash - price;
  for (let i = 0; i < currency.length; i++){
      if (remainder < currency[i]){
        if (dic[currencyValues[currency[i]]] == 0){
           changedValues.push([currencyValues[currency[i]], 0])
        }
          continue
       } else {
          let money = dic[currencyValues[currency[i]]];
          if (money == 0) {
            changedValues.push([currencyValues[currency[i]], money]);
            changedValuesDic[currencyValues[currency[i]]] = money;
            continue
          } else if (remainder > money) {
            // need toFixed because floating point issue
            remainder = (remainder - money).toFixed(2);
            changedValues.push([currencyValues[currency[i]], money])
            changedValuesDic[currencyValues[currency[i]]] = remainder;
          } else if (remainder == money) {
            
            changedValues.push([currencyValues[currency[i]], money])
            changedValuesDic[currencyValues[currency[i]]] = 0;;           remainder = 0;
            break;
            
          } else if (remainder < money) {

            let amountBills = Math.floor(remainder / currency[i])
            // need toFixed because floating point issue
            remainder = (remainder % currency[i]).toFixed(2);
            changedValuesDic[currencyValues[currency[i]]] = money;
            changedValues.push([currencyValues[currency[i]], currency[i] * amountBills])

            if (remainder == 0){
                break;
            } 
            
          }
      }
    }
    // check to see insufficent funds
    if (remainder !=0) {
      return {status: "INSUFFICIENT_FUNDS", change: []};
    }

    // check to see if cash register is deleted non-insufficent
   
    if (Object.keys(changedValuesDic).every((key) => {
      return changedValuesDic[key] == 0 ;
    })) {
      // must reverse the order for closed
      change["status"] = "CLOSED";
      change["change"] = changedValues.reverse();
    } else {
      change["status"] = "OPEN";
      change["change"] = changedValues;
    }
  
  return change;
}

checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
