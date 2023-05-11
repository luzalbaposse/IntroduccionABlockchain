// SPDX-License-Identifier: MIT
// Contrato para dividir pagos entre un grupo de personas
pragma solidity >=0.7.0 <0.9.0;
contract DividirGastos{
    address payable[] public cuentas; // arreglo de cuentas
    uint256 public totalCuentas; // total de cuentas
    mapping(address => uint256) public balances; // mapeo de balances
    address public creador; // dirección del creador
    constructor(address payable[] memory _cuentas) {
        creador = msg.sender; // guardo la dirección del creador
        cuentas = _cuentas; // guardo las cuentas
        totalCuentas = _cuentas.length; // guardo el total de cuentas
    }
    function dividir() public payable { // función que divide el pago
        require(msg.sender == creador); // verifico que el que llama a la función sea el creador
        uint256 monto = msg.value / totalCuentas; // calculo el monto a pagar
        for (uint256 i = 0; i < totalCuentas; i++) { // recorro las cuentas
            balances[cuentas[i]] += monto; // incremento el balance de la cuenta
        }
    }
    function retirar() public { // función que retira el pago
            uint256 balance = balances[msg.sender]; // guardo el balance de la cuenta
        balances[msg.sender] = 0; // pongo el balance en cero
        //transfiero el balance a la cuenta
        (bool success, ) = msg.sender.call{value: balance}("");
    }
}