/* Return the provided string with the first letter of each word capitalized.
 * Make sure the rest of the word is in lower case.
 * */

function titleCase(str) {
  let newArray = str.split(" ");
  str = str;

  for (let i = 0; i < newArray.length; i++) {
    let re = new RegExp(newArray[i]);
    str = str.replace(re, newArray[i].toLowerCase());
    let re2 = new RegExp(newArray[i].toLowerCase());
    let reMatch = str.match(re2);

    str = str.replace(re2, reMatch[0][0].toUpperCase() + reMatch[0].slice(1));
  }

  return str;
}
