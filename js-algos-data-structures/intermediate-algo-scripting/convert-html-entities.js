function convertHTML(str) {
  let conversion = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&apos;"
  }

  let re = /&|<|>|\"|\'/g
  let matchedItems = str.match(re)

  console.log(matchedItems)


  if (matchedItems == null) {
   
    return str
  } else {

    for (let i = 0; i < matchedItems.length; i++) {
    let regex = new RegExp(matchedItems[i], "ig")
    str = str.replace(regex, conversion[matchedItems[i]])
  }
  return str;


  }

  
}

convertHTML("Schindler's List");
