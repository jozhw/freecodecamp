function rot13(str) {
  let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")
  let re = /[A-Z]/g

  let decipher = str.split("").map( (letter) => {
    if (Boolean(letter.match(re)) == true) {
      let index = alphabet.indexOf(letter);
      if (index + 13 > 25) {
        // from 13 - 25 - 1
        let remainder = index - 13;
        return alphabet[remainder]

      } else {
        return alphabet[index + 13]
      }

    } else {
      return letter
    }

  }

  )
  return decipher.join("");
}

rot13("SERR PBQR PNZC");
