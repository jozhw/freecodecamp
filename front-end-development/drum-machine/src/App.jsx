import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [activeKey, setActiveKey] = useState("");
  useEffect(() => {
    document.addEventListener("keydown", (event) => {
      play(event.key.toUpperCase());
    });
  });

  const drums = [
    {
      key: "Q",
      audio: "https://s3.amazonaws.com/freecodecamp/drums/Heater-1.mp3",
      id: 0,
    },

    {
      key: "W",
      audio: "https://s3.amazonaws.com/freecodecamp/drums/Heater-2.mp3",
      id: 1,
    },

    {
      key: "E",
      audio: "https://s3.amazonaws.com/freecodecamp/drums/Heater-3.mp3",
      id: 2,
    },

    {
      key: "A",
      audio: "https://s3.amazonaws.com/freecodecamp/drums/Heater-4_1.mp3",
      id: 3,
    },
    {
      key: "S",
      audio: "https://s3.amazonaws.com/freecodecamp/drums/Heater-6.mp3",
      id: 4,
    },
    {
      key: "D",
      audio: "https://s3.amazonaws.com/freecodecamp/drums/Dsc_Oh.mp3",
      id: 5,
    },
    {
      key: "Z",
      audio: "https://s3.amazonaws.com/freecodecamp/drums/Kick_n_Hat.mp3",
      id: 6,
    },
    {
      key: "X",
      audio: "https://s3.amazonaws.com/freecodecamp/drums/RP4_KICK_1.mp3",
      id: 7,
    },

    {
      key: "C",
      audio: "https://s3.amazonaws.com/freecodecamp/drums/Cev_H2.mp3",
      id: 8,
    },
  ];
  const play = (selector) => {
    const audio = document.getElementById(selector);
    audio.play();
    setActiveKey(selector);
  };
  return (
    <div id="drum-machine">
      <div id="display">{activeKey}</div>
      <div className="drum-pads">
        {drums.map((drum) => (
          <div
            className="drum-pad"
            onClick={() => play(drum.key)}
            id={drum.audio}
          >
            {drum.key}
            <audio className="clip" id={drum.key} src={drum.audio}></audio>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
