import React from "react";
import { Link } from "react-router-dom";

function NavBar() {
    return (
        <>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <Link to="/" style={{textDecoration: "none"}}> <a class="navbar-brand">PyTypeCraft</a>
                </Link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <Link to="/index" style={{textDecoration: "none"}}> <a class="nav-link active" aria-current="index">Home</a>
                </Link>
                <Link to="/analisis" style={{textDecoration: "none"}}> <a class="nav-link active" aria-current="analisis">Análisis</a>
                </Link>
                <Link to="/reportes" style={{textDecoration: "none"}}> <a class="nav-link active" aria-current="reportes">Reportes</a>
                </Link>
            </ul>
            </div>
        </div>
        </nav>
    </>
    )
}

export default NavBar;