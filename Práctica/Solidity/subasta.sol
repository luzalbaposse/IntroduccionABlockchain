
// SPXD-License-Identifier: MIT
// Contrato para hacer una subasta simple dado un NFT y un tiempo de duración
pragma solidity >=0.7.0 <0.9.0;

contract Subasta{
    address public ganador; // dirección del ganador
    uint256 public ofertaActual; // oferta actual
    uint256 public tiempoFinal; // tiempo final
    uint256 public duracion; // duración
    mapping(address => uint256) public balances; // mapeo de balances

    function registrar() public payable { // función que registra una oferta
        require(msg.value > ofertaActual); // verifico que la oferta sea mayor a la actual
        require(block.timestamp < tiempoFinal); // verifico que el tiempo no haya finalizado
        require(msg.sender != ganador); // verifico que el que llama a la función no sea el ganador
        if (ganador != address(0)) { // verifico que el ganador no sea la dirección cero
            balances[ganador] += ofertaActual; // incremento el balance del ganador
        }
        ganador = msg.sender; // guardo el ganador
        ofertaActual = msg.value; // guardo la oferta actual
        tiempoFinal = block.timestamp + duracion; // guardo el tiempo final
    }

    function retirar() public { // función que retira el pago
        require(msg.sender != ganador); // verifico que el que llama a la función no sea el ganador
        uint256 balance = balances[msg.sender]; // guardo el balance de la cuenta
        balances[msg.sender] = 0; // pongo el balance en cero
        //transfiero el balance a la cuenta
        (bool success, ) = msg.sender.call{value: balance}("");
    }

}