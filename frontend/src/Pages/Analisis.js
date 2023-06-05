import React from "react";
import NavBar from "../Components/NavBar.js";
import Consola from "../Components/Editor.js";
import Service from "../Services/Service.js";

function Analisis() {
  const [value, setValue] = React.useState("");
  const [response, setResponse] = React.useState("");

  const changeText = (text) => {
    setValue(text);
  }

  const handlerClick = () => {
    Service.comando(value)
    .then((respuesta) => {
      setResponse(respuesta.respuesta);
      console.log(respuesta);
    })
  }

  const handlerLimpiar = () => {
    setResponse("");
    changeText("");
  }

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
      setValue(event.target.result);
    };

    reader.readAsText(file);
  };

  const handleLoadClick = () => {
    const input = document.createElement("input");
    input.type = "file";
    input.accept = ".ts";
    input.addEventListener("change", handleFileChange);
    input.click();
  };


  return (
    <>
      <NavBar />
      <h1>Proyecto 1 - TypeCraft - 202000343 - 202004745</h1> 
      <Consola text={"Consola Entrada"} handlerChange = {changeText} value ={value} rows={15} />
      <div class ="container">
      <button type="button" class="btn btn-primary" onClick={handlerClick}>Ejecutar</button>
      <button type="button" class="btn btn-primary" onClick={handleLoadClick}>Cargar archivo</button>
      <button type="button" class="btn btn-danger" onClick={handlerLimpiar}>Limpiar</button>
      </div>      
      <Consola text={"Consola Salida"} value = {response} rows={10}  readOnly/>
    </>
  );
}

export default Analisis;