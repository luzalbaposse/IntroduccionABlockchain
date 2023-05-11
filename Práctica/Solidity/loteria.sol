// SPDX-License-Identifier: MIT
// Contrato de una loteria: voy a sortear un número aleatorio entre 1 y 10, y si coincide con el número que elija el usuario, gana
pragma solidity >=0.7.0 <0.9.0;

contract Loteria {
    uint256 public numeroGanador; // variable para almacenar el número ganador
    uint256 public contador = 0; // contador para saber cuantos números se han jugado
    address public ganador; // dirección del ganador
    uint256 public premio; // premio que se lleva el ganador

    function jugar(uint256 _numero) public payable { // función para jugar
        require(msg.value >= 1 ether, "No has apostado lo suficiente"); // requiero que el usuario apueste al menos 1 ether
        require(_numero >= 1 && _numero <= 10); // requiero que el número esté entre 1 y 10
        contador += 1; // incremento el contador
        if (contador == 1) { // si es el primer número que se juega
            numeroGanador = uint256(keccak256(abi.encodePacked(block.timestamp))) % 10 + 1; // genero un número aleatorio entre 1 y 10
        }
        if (_numero == numeroGanador) { // si el número que ha elegido el usuario coincide con el número ganador
            ganador = msg.sender; // el ganador es el usuario que ha jugado
            premio = address(this).balance; // el premio es el balance del contrato
        }
    }

    function retirar() public { // función para retirar el premio
        require(msg.sender == ganador, "No eres el ganador"); // requiero que el usuario sea el ganador
        payable(msg.sender).transfer(premio); // transfiero el premio al usuario
    }
}