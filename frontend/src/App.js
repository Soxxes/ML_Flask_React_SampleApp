import React, { useState } from "react";

function App() {
  const [inputText, setInputText] = useState("");
  const [data, setdata] = useState({
      result: 0,
  });

  // Using useEffect for single rendering
  function test(x) {
    // flask server it will be redirected to proxy
    fetch("/predict", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            X: x
        })
    }).then((res) =>
        res.json().then((data) => {
            // Setting a data from api
            setdata({
                result: data.prediction
            });
        })
    );
}

  return (
    <div style={{ marginTop: "10%", textAlign: "center" }}>
      <input value={inputText} onChange={(e) => setInputText(e.target.value)} />
      <button onClick={() => test(inputText)}>Click me</button>
      <p>{data.result}</p>
    </div>
  );
}

export default App;
