function palindrome(str) {
  let re = /[\W_]/g
  let replacedString = str.replace(re, "").toLowerCase()

  let determinePalin = replacedString.split("")
          .reverse()
          .join("");
  console.log(determinePalin)
  if (determinePalin == replacedString) {
    return true;
  } else {
    return false;
  }

}

palindrome("1 eye for of 1 eye.");