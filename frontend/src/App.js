import React, { useState } from "react";

function App() {
  const [inputText, setInputText] = useState("");
  const [data, setdata] = useState({
      result: 0,
  });

  function test(x) {
    // flask server will be redirected to proxy
    fetch("/predict", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            X: x
        })
    }).then((res) =>
        res.json().then((data) => {
            // setting data from api
            setdata({
                result: data.prediction
            });
        })
    );
}

  return (
    <div style={{ marginTop: "10%", textAlign: "center" }}>
      <input value={inputText} onChange={(e) => setInputText(e.target.value)} />
      <button onClick={() => test(inputText)}>Predict</button>
      <p>{data.result}</p>
    </div>
  );
}

export default App;
