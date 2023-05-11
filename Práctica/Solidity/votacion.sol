// SPDX-License-Identifier: MIT
// Contrato para votar a un candidato
pragma solidity >=0.7.0 <0.9.0;

contract Votacion {
    struct Candidato { // estructura de un candidato
        string nombre; // nombre del candidato
        uint256 votos; // votos del candidato
    }

    mapping(uint256 => Candidato) public candidatos; // mapeo de candidatos
    uint256 public candidatosContador; // contador de candidatos

    constructor() {
        agregarCandidato("Candidato 1"); // agrego un candidato
        agregarCandidato("Candidato 2"); // agrego un candidato
    }

    function agregarCandidato(string memory _nombre) private { // función que agrega un candidato
        candidatosContador++; // incremento el contador de candidatos
        candidatos[candidatosContador] = Candidato(_nombre, 0); // creo un candidato
    }

    function votar(uint256 _candidatoId) public { // función que vota a un candidato
        require(_candidatoId > 0 && _candidatoId <= candidatosContador); // verifico que el candidato exista
        candidatos[_candidatoId].votos++; // incremento los votos del candidato
    }
}