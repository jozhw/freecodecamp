let sampleWord = "astronaut";
let pwRegex = /(?=\w{6,})(?=\D*\d{2,})/; // Change this line
let result = pwRegex.test(sampleWord);

// must use the \D because otherwise it will only match the consecutive digits
// for lookheads, the parenthesis are separate statements
// for example, the first statement matches an alphanumeric including _ that occurs at least 6 times in a row
// for the second it matches that contains at least 2 digits in a row
