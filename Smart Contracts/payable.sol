// SPDX-License-Identifier: MIT 
pragma solidity ^0.8.10;

contract Owner {
   address owner;

   constructor() {
      owner = msg.sender;
   }

   modifier onlyOwner() { // Modificador de acceso
      require(msg.sender == owner, "Podes llamar solo si sos owner :)"); // Si no es owner, no puede ejecutar la función
      _;
   }
}

contract Register is Owner { // Hereda de Owner
   mapping (address => bool) registeredAddresses;
   uint price; // Precio para registrarse

   constructor(uint initialPrice) {
      price = initialPrice;
   }

   function register() public payable costs(price) {
      registeredAddresses[msg.sender] = true;
   }

   function changePrice(uint _price) public onlyOwner {
      price = _price;
   }

   function isRegistered(address _address) public view onlyRegistered returns (bool) { // Solo los registrados pueden ejecutar esta función
      return registeredAddresses[_address];
   }

   modifier costs(uint _amount) {
      require(msg.value >= _amount, "No tenes fondos suficientes");
      _; // Ejecuta la función si tiene fondos suficientes

      if (msg.value > _amount) { // Si tiene más fondos, se le devuelve el excedente
         uint refundAmount = msg.value - _amount;
         payable(msg.sender).transfer(refundAmount);
      }
   }

   modifier onlyRegistered() { // Modificador de acceso
      require(registeredAddresses[msg.sender], "Solo los registrados pueden ejecutar"); // Si no está registrado, no puede ejecutar la función
      _;
   }
}
