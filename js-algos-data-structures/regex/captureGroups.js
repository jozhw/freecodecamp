let repeatNum = "42 42 42";
let reRegex = /^(\d+) \1 \1$/; // Change this line
let result = reRegex.test(repeatNum);

// must have the $ to match the end because the group matching only occurs for at least 3 otherwise
