import { useState } from "react";
import "./App.css";

function App() {
  const [display, setDisplay] = useState("0");
  const [calculate, setCalculate] = useState("0");
  const operations = [
    { value: 0, id: "zero" },

    { value: 1, id: "one" },

    { value: 2, id: "two" },

    { value: "*", id: "multiply" },

    { value: 3, id: "three" },

    { value: 4, id: "four" },

    { value: 5, id: "five" },

    { value: "/", id: "divide" },

    { value: 6, id: "six" },

    { value: 7, id: "seven" },

    { value: 8, id: "eight" },

    { value: "+", id: "add" },

    { value: 9, id: "nine" },

    { value: ".", id: "decimal" },

    { value: "=", id: "equals" },

    { value: "-", id: "subtract" },
  ];

  const handler = (event) => {
    const operator = event.target.textContent;

    if (!isNaN(operator)) {
      if (display === "0") {
        setDisplay(operator);
      } else {
        setDisplay(display + operator);
      }
    } else {
      switch (operator) {
        case ".":
          const array = display.split(" ");
          const lastItem = array[display.length - 1];
          if (!lastItem.includes(".")) {
            setDisplay(display + operator);
            break;
          }
          break;
        case "=":
          const arr = display.split(" ").filter((value) => value);
          const newArr = [];
          const specialOperators = ["+", "*", "/", "-"];
          for (let i = 0; i < arr.length; i++) {
            console.log(newArr);
            if (specialOperators.includes(arr[i])) {
              if (
                specialOperators.includes(newArr[i - 1]) &&
                newArr[i - 1] != "-" &&
                arr[i] != "+"
              ) {
                newArr[i - 1] = arr[i];
              } else {
                newArr.push(arr[i]);
              }
            } else {
              newArr.push(arr[i]);
            }
          }

          setCalculate(newArr.join(" "));

          setDisplay(eval(newArr.join(" ")));
          break;

        default:
          setDisplay(display + " " + operator + " ");
          break;
      }
    }
  };

  const handleClear = () => {
    setDisplay("0");
  };

  return (
    <div className="App">
      <div className="calculator">
        <div className="viewer" id="display">
          {display}
        </div>
        <div className="viewer" id="clear" onClick={handleClear}>
          AC
        </div>
        <div className="operators">
          {operations.map((operation) => (
            <div
              className="operator"
              id={operation.id}
              onClick={(e) => handler(e)}
            >
              {operation.value}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
