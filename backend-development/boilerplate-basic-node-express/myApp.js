let bodyParser = require('body-parser')
let express = require('express');
let app = express();
console.log("Hello World");



// parse post requests
app.use(bodyParser.urlencoded({ extended: false }));

// post req
app.route('/name')
  .post((req, res) => {
  const {first: firstname, last: lastname} = req.body;
    res.json({name: `${firstname} ${lastname}`});
  
})



// middleware
app.get('/now', (req, res, next) => {
  req.time = new Date().toString();
  next();
}, (req, res) => {
  res.send({time: req.time})
});

app.use("/public", express.static(__dirname + '/public'));

app.use((req, res, next) => {
  let string = req.method + " " + req.path + " - " + req.ip;
  console.log(string)
  next();
  
})

// echo server
app.get("/:word/echo", (req, res) => {
  const {word} = req.params
  
  res.json({
    echo: word
  })
  
})

// get name
app.route('/name')
  .get((req, res) => {
  const {first: firstName, last: lastName} = req.query;
  
  res.json({
    name: `${firstName} ${lastName}`
  });
})



// first argument of get is the trigger
app.get("/", (req, res) => { res.sendFile(__dirname + '/views/index.html')});
app.get("/json", (req, res) => { 
  if (process.env.MESSAGE_STYLE == "uppercase"){
    res.json({
      "message": "Hello json".toUpperCase()
    })
    
  } else {
     res.json({
  "message": "Hello json"
})
    
  }
  
 });






































 module.exports = app;
