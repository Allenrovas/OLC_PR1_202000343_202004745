import React from "react";
import NavBar from "../Components/NavBar.js";
import desarrolladores from "../Images/Desarrolladores.jpeg";


function Index() {

  return (
    <>
      <NavBar />
      <h1>Proyecto 1 - PyTypeCraft - OLC2 </h1>
      <h1>Desarrolladores</h1>
      <h2 class="rainbow-text">Luis Manuel Chay Marroquín - 202000343</h2>
      <h2 class="rainbow-text">Allen Giankarlo Román Vásquez - 202004745</h2>
       <img src={desarrolladores} alt="desarrolladores" />
    </>
  );
}

export default Index;