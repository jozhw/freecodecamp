import { useState, useEffect } from "react";
import "./App.css";
import audio from "./assets/classic-alarm-995.wav";

function App() {
  const [breakLength, setBreakLength] = useState(5);
  const [sessionLength, setSessionLength] = useState(25);
  const [timer, setTimer] = useState(1500);
  const [timerStatus, setTimerStatus] = useState(false);
  const [onBreak, setOnBreak] = useState(false);

  useEffect(() => {
    if (timerStatus) {
      const interval = setInterval(() => {
        setTimer((oldTime) => {
          const newTime = oldTime - 1;
          if (newTime < 1) {
            setTimerStatus(false);
            document.getElementById("beep").play();
            setOnBreak(true);
            return breakLength * 60;
          }
          return newTime;
        });
      }, 1000);
      return () => {
        clearInterval(interval);
      };
    } else if (onBreak) {
      const interval = setInterval(() => {
        setTimer((oldTime) => {
          const newTime = oldTime - 1;
          if (newTime < 1) {
            setOnBreak(false);
            if (sessionLength > 0) {
              setTimerStatus(true);
              return sessionLength * 60;
            }
          }
          return newTime;
        });
      }, 1000);
      return () => {
        clearInterval(interval);
      };
    }
  }, [timerStatus, onBreak]);

  const handleTimerOn = () => {
    setTimerStatus(true);
  };

  const handleTimerOff = () => {
    setTimerStatus(false);
  };

  const handleReset = () => {
    setBreakLength(5);
    setOnBreak(false);
    setSessionLength(25);
    setTimerStatus(false);
    setTimer(1500);

    document.getElementById("beep").pause();
  };

  const handleBreakDecrement = () => {
    if (breakLength > 1 && !timerStatus) {
      setBreakLength(breakLength - 1);
    }
  };

  const handleSessionDecrement = () => {
    if (sessionLength > 1 && !timerStatus) {
      setSessionLength(sessionLength - 1);
      setTimer(timer - 60);
    }
  };

  const handleBreakIncrement = () => {
    if (!timerStatus && breakLength < 60) {
      setBreakLength(breakLength + 1);
    }
  };

  const handleSessionIncrement = () => {
    if (sessionLength < 60 && !timerStatus) {
      setSessionLength(sessionLength + 1);
      setTimer(timer + 60);
    }
  };

  return (
    <>
      <div>
        <div id="timer-label">{onBreak ? "Break" : "Session"}</div>
        <div id="time-left">
          {Math.floor(timer / 60) < 10
            ? "0" + Math.floor(timer / 60)
            : Math.floor(timer / 60)}
          :{timer % 60 < 10 ? "0" + (timer % 60) : timer % 60}
        </div>
      </div>
      <div>
        <div id="session-label">Session Length</div>
        <div id="session-length">{sessionLength}</div>
        <button id="session-increment" onClick={handleSessionIncrement}>
          +
        </button>
        <button id="session-decrement" onClick={handleSessionDecrement}>
          -
        </button>
      </div>

      <div>
        <div id="break-label">Break Length</div>
        <div id="break-length">{breakLength}</div>
        <button id="break-increment" onClick={handleBreakIncrement}>
          +
        </button>
        <button id="break-decrement" onClick={handleBreakDecrement}>
          -
        </button>
      </div>
      <div>
        {timerStatus ? (
          <button onClick={handleTimerOff} id="start_stop">
            Pause
          </button>
        ) : (
          <button onClick={handleTimerOn} id="start_stop">
            Start
          </button>
        )}
        <button onClick={handleReset} id="reset">
          Reset
        </button>

        <audio id="beep" preload="auto" src={audio} />
      </div>
    </>
  );
}

export default App;
