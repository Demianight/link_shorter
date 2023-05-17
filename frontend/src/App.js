import Form from "./components/Form";
import "bootstrap/dist/css/bootstrap.css";
import Header from "./components/Header";
import "./App.css";

function App() {
  return (
    <div className="text-center box">
      <div className="container objects">
        <Header />
        <Form />
      </div>
    </div>
  );
}

export default App;
