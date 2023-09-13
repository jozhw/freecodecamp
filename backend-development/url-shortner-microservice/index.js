require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();

// Basic Configuration
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.urlencoded({extended: true}))


app.use('/public', express.static(`${process.cwd()}/public`));

app.get('/', function(req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

// Your first API endpoint
app.get('/api/hello', function(req, res) {
  res.json({ greeting: 'hello API' });
});

const originalUrls = [];
const shortUrls = []

app.post('/api/shorturl', (req, res) => {
  
  const url = req.body.url;
  const indexUrl = originalUrls.indexOf(url);
  
  if (!url.includes("https://") && !url.includes("http://") ){
    return res.json({
      error: 'invalid url'
    })
  }
  
  
  if ( indexUrl < 0){
    originalUrls.push(url);
    shortUrls.push(shortUrls.length);
    return  res.json({original_url: url, short_url: shortUrls.length - 1})
    
  }
  
  return res.json({original_url: url, short_url: shortUrls[indexUrl]})
  
})


app.get('/api/shorturl/:short', (req, res) => {
  
  const shortUrl = shortUrls.indexOf(parseInt(req.params.short));
  if (shortUrl < 0 ){
    return res.json({
      error: "No such shorturl exists"
    })
  }
  
  res.redirect(originalUrls[shortUrl])

  
  
  
  
})

app.listen(port, function() {
  console.log(`Listening on port ${port}`);
});
