// SPDX-License-Identifier: MIT

pragma solidity 0.5.2;

import 'https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol';

contract Token is ERC20Mintable{
        string public name = "LUZ";
        string public symbol = "LZ";
        uint8 public decimals = 4;
}