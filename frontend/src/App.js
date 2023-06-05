import './App.css';
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Index from "./Pages/index.js";
import Analisis from "./Pages/Analisis.js";
import Reportes from "./Pages/Reportes.js";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Index />} />
        <Route path="/reportes" element={<Reportes />} />
        <Route path="/analisis" element={<Analisis />} />
        <Route path="*" element={<Navigate to="/" replace={true} />} exact = {true} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
