// SPDX-License-Identifier: MIT
// Contrato que almacena y recupera de un entero 
pragma solidity >=0.7.0 <0.9.0;

contract Almacenamiento {
    uint256 numero; // variable de estado

    function guardar(uint256 _num) public { // función que guarda un número
        numero = _num;
    }

    function recuperar() public view returns (uint256) { // función que recupera el número guardado
        return numero;
    }
}