// SPDX-License-Identifier: MIT
// Contrato para registrar nombres 
pragma solidity >=0.7.0 <0.9.0;

contract Registro {
    string[] public nombres; // array de strings para almacenar los nombres
    uint256 public contador = 0; // contador para saber cuantos nombres hay registrados

    function registrar(string memory _nombre) public { // función para registrar nombres
        nombres.push(_nombre); // añado el nombre al array
        contador += 1; // incremento el contador
    }
}
