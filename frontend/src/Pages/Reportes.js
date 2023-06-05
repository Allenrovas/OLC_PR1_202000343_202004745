import React from "react";
import NavBar from "../Components/NavBar.js";
import Service from "../Services/Service.js";
import Graphviz from "graphviz-react";

function Reportes() {
  const [response, setResponse] = React.useState("");
  const [graphCode, setGraphCode] = React.useState("");
  
  
  const handleGraphClick = (url) => {
    Service.imagen(url)
    .then((response) => {
      setGraphCode(response.respuesta);
      console.log(response);
    
    })
    
  }

 

  return (
    <>
      <NavBar />
      <h1>Proyecto 1 - Reportes PyTypeCraft - OLC2 </h1>
      <div class ="container" >
        <button type="button" class="btn btn-primary">Reporte de Errores</button>
        <button type="button" class="btn btn-primary">Reporte de Tabla de Símbolos</button>
        <button type="button" class="btn btn-primary">Reporte de AST</button>
      </div>
      <div style={{ width: "100%", height: "100%" }}>
          {graphCode && (
      <Graphviz
        dot={graphCode}
        options={{ width: "100%", height: "auto", zoom: 1 }}
        onLoad={() => console.log("Loaded Graphviz")}
        onClick={() => console.log("Clicked Graphviz")}
        onError={(error) => console.error(error)}
        zoomable
      />
    )}
      </div>
    </>
  );
}

export default Reportes;