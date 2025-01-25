import { useState } from "react";
import "./global.css";

function App() {
	const [data, setData] = useState("");
	const callApi = async () => {
		try {
			const response = await fetch("/api/read");
			const json = await response.json();
			setData(json);
		} catch (error) {
			console.error(error);
		}
	};
	return (
		<>
			<h1 onClick={() => callApi()}>Home</h1>
			<h2>Data: {data}</h2>
		</>
	);
}

export default App;
