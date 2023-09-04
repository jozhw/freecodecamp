import React from "react";
import "./styles.css";
import { useState, useEffect } from "react";

export default function App() {
  const [quote, setQuote] = useState({});

  const getQuote = async () => {
    try {
      await fetch("https://api.quotable.io/quotes/random")
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          data = data[0];
          setQuote({
            quote: data.content,
            author: data.author
          });
        });
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getQuote();
  }, []);

  return (
    <div>
      <div className="App">
        <div id="quote-box" className="quote-box">
          <div id="text">{quote.quote}</div>
          <div id="author">{quote.author}</div>

          <button onClick={getQuote} id="new-quote">
            New Quote
          </button>
          <a
            id="tweet-quote"
            href={
              "https://twitter.com/intent/tweet?hashtags=quotes&related=freecodecamp&text=" +
              quote.quote
            }
            target="_blank"
            rel="noreferrer"
          >
            Twitter
          </a>
        </div>
      </div>
    </div>
  );
}
