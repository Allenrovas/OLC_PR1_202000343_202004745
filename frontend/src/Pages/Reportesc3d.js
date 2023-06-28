import React from "react";
import NavBar from "../Components/NavBar.js";
import Service from "../Services/Service.js";
import Graphviz from "graphviz-react";
import { useState } from "react";

function Reportesc3d() {
  const [graphCode, setGraphCode] = React.useState("");
  const [arregloErrores, setArregloErrores] = useState([]);
  const [arregloSimbolos, setArregloSimbolos] = useState([]);
  const [tablaSimbolosVisible, setTablaSimbolosVisible] = useState(false);
  const [tablaErroresVisible, setTablaErroresVisible] = useState(false);
  
  
  const handleGraphClick = (url) => {
    Service.imagen(url)
    .then((response) => {
      
      setGraphCode(response.respuesta);
      console.log(response);
    
    })
    
  }

  const reporteErrores = () => {
    Service.reportesc3d()
    .then((response) => {
      setArregloErrores([]);
      if(response.Errores !== undefined){
        setTablaSimbolosVisible(false);
        setTablaErroresVisible(true);
        setArregloErrores(prevArreglo => [...prevArreglo, ...response.Errores]);        }  

      
    })
    }

    const reporteTabla = () => {
      Service.reportesc3d()
      .then((response) => {
        setArregloSimbolos([]);
        if(response.Simbolos !== undefined){
          setTablaSimbolosVisible(true);
          setTablaErroresVisible(false);
          setArregloSimbolos(prevArreglo => [...prevArreglo, ...response.Simbolos]);        
          
        }
      })
      }


 

  return (
    <>
      <NavBar />
      <h1>Proyecto 2 - Reportes PyTypeCraft - OLC2 </h1>
      <div class ="container" >
        <button onClick={reporteErrores} type="button" class="btn btn-primary">Reporte de Errores</button>
        <button onClick={reporteTabla} type="button" class="btn btn-primary">Reporte de Tabla de Símbolos</button>
      </div>
      {tablaErroresVisible && (
        <table class="table table-striped">
          <thead>
            <tr>
              <th>Tipo</th>
              <th>Descripcion</th>
              <th>Fila</th>
              <th>Columna</th>
              <th>Hora</th>
            </tr>
          </thead>
          <tbody>
        {arregloErrores.map((item, index) => (
          <tr key={index}>
            {item.split(',').map((columna, colIndex) => (
              <td key={colIndex}>{columna}</td>
            ))}
          </tr>
        ))}
      </tbody>
        </table>
      )}
            {tablaSimbolosVisible && (
        <table class="table table-striped">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Valor</th>
              <th>Tipo</th>
              <th>Ambito</th>
              <th>Fila</th>
              <th>Columna</th>
            </tr>
          </thead>
          <tbody>
        {arregloSimbolos.map((subarreglo, index) => (
            <tr key={index}>
              {subarreglo.map((dato, colIndex) => (
                <td key={colIndex}>{dato}</td>
              ))}
            </tr>
          ))}
      </tbody>
        </table>
      )}
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

export default Reportesc3d;