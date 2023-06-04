// SPDX-License-Identifier: MIT

pragma solidity ^0.8.10;

contract Pokemon {
  uint private capturedPokemons = 0;

  function sucess() public view returns (bool) { 
    return capturedPokemons > 5;
  }
  function getCaptured() external view returns(uint) {
    return capturedPokemons;
  }
  function init() private {
    capturedPokemons=0;
  }
  function capture() internal {
    capturedPokemons++;
    //getCaptured(); 
    sucess();
  }
}

contract Pikachu is Pokemon {
  uint private pikachuEncounters;

  function PikachuEncounter() public returns (uint) {
    pikachuEncounters++;
    capture();
    sucess();
    return pikachuEncounters;
  }
}

contract ExternalContract {
  Pokemon private pok;

  constructor() {
    pok = new Pokemon();
  }  
   
  function getAmountCaptured() public view returns (uint) { 
    pok.sucess();
    return pok.getCaptured(); 
  }
}

contract CapturedChecker { // Este contrato cambia la implementación de Pokemon
  Pokemon private pok;

  constructor() { // Nuevo contrato Pokemon
    pok = new Pokemon();
  }  

  function replacePokemon(address _newPokemonAddress) public { // Cambia la implementación de Pokemon
    pok = Pokemon(_newPokemonAddress); // Cambia la implementación porque se le pasa la dirección del nuevo pikachu
  }

  function getAmountCaptured() public view returns (uint) { // Devuelve el número de pokemons capturados
    pok.sucess(); 
    return pok.getCaptured(); // Llama a la función del contrato Pokemon
  }
}

contract Pikatrucho is Pokemon { // Pikatrucho hereda de Pokemon
  uint private pikatruchoEncounters; // Añade una variable que no tiene Pokemon

  function sucess() public view override returns (bool) { // 
    return false; // Cambia la implementación de la función sucess
  }

  function PikatruchoEncounter() public returns (uint) { // Añade una función que no tiene Pokemon
    pikatruchoEncounters++; // Añade encounters pero no llama a capture -> no se incrementa capturedPokemons
    sucess(); // Sucess devuelve false
    return pikatruchoEncounters;
  }
}

