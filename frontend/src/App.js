import { use, useEffect, useState } from "react";

function App() {
  const [data, setData] = useState("Bu veri backendden geldi");
  useEffect(() => {
    fetch("http://127.0.0.1:5000")
    .then((res)=>res.json())
    .then((data)=>setData(data.message))
  }, []);
  return (
    <div >
      <h1>{data}</h1>
    </div>
  );
}

export default App;
