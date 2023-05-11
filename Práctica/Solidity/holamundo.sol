// SPDX-License-Identifier: MIT
// Contrato que dice hola mundo
pragma solidity >=0.7.0 <0.9.0;

contract MyContract {
    function helloWorld() public pure returns (string memory) { // defino la función helloWorld
        return "Hello, World!"; // 
    }
}
