function telephoneCheck(str) {
  let reAlpha = /[a-zA-Z]/g;
  let reSpecial = /[^\w-\s]/g;
  let rePara = /\(\d{3}\)/g;
  let reNotPara = /\(.{3}\)/g
  let reReplace = /[^0-9]/g;
  let reFirst = /^[^0-9/(]/;
  let reDash = /-[\d]{5,}|^[^1]{1}-|\s[\d]{2}-/g
  let reIfDash = /-/g

  // eliminate easy non phone #s
  if (Boolean(str.match(reAlpha)) == true || Boolean(str.match(reFirst)) == true){
    return false;
  }

  // cases for special characters "()"
  if (Boolean(str.match(reSpecial)) == true){
    if (Boolean(str.match(rePara)) == false || str.match(rePara).length > 1 || str.match(reNotPara).length > 1) {

      return false
    }
  }


  let rawStr = str.replace(reReplace, "")

  // after the rawStr adjustment the str is either 10 or 11
  // if it is 11 then 1 must be first

  if (rawStr.length == 11) {
    if (rawStr[0] != 1){
      return false;
    }
  } else if (rawStr.length < 10 || rawStr.length > 11){
    return false;
  }

   console.log(str.match(reDash))

  if (Boolean(str.match(reIfDash)) == true) {
    if (Boolean(str.match(reDash)) == true){
      return false
    }
  }

 
  return true;
}

telephoneCheck("1 555-555-5555");