function convertToRoman(num) {

const hundred = {
    0: "",
    1 : "C",
    4 : "CD",
    5: "D",
    9: "CM"
};

const ten = {
  0: "",
  1 : "X",
  4: "XL",
  5: "L",
  9: "XC",
};

const one = {
  0: "",
  1: "I",
  4: "IV",
  5: "V",
  9: "IX"
};


const str = num.toString();
const length = str.length;

let thousands = 0;
let hundreds = 0;
let tens = 0;
let ones = 0;

let array = [];

if (length >= 4) {
  thousands = str.slice(0, length - 3);
  array.push("M".repeat(thousands));

  hundreds = str.slice(length - 3, length - 2);
  array.push(conversion(hundreds, hundred));

  tens = str.slice(length - 2, length - 1);
  array.push(conversion(tens, ten));

  ones = str.slice(length - 1, length);
  array.push(conversion(ones, one));


} else if (length == 3) {
  hundreds = str.slice(0, length - 2);
  array.push(conversion(hundreds, hundred));

  tens = str.slice(length - 2, length - 1);
  array.push(conversion(tens, ten));

  ones = str.slice(length - 1, length);
  array.push(conversion(ones, one));
} else if (length == 2) {
  tens = str.slice(0, length - 1);
  array.push(conversion(tens, ten));

  ones = str.slice(length - 1, length);
  array.push(conversion(ones, one));

} else {
  ones = str.slice(0,)
  array.push(conversion(ones, one));
}

function conversion(number, roman) {

  if (number == 9) {
    return roman[number];
  } else if (number > 5) {
     return roman["5"] + roman["1"].repeat(number - 5);
  } else if (number == 5) {
      return roman[number];
  } else if (number == 4) {
      return roman[number];
  } else {
    return roman["1"].repeat(number);
  }
  
}

 return array.join("");
}

convertToRoman(4600);

console.log(convertToRoman(4600))