//SPDX-License-Identifier:MIT
pragma solidity ^0.4.16;


contract Ownable{
 address public owner;
 

function Ownable() {
 owner = msg.sender ;
 }

 modifier onlyOwner() {
 require(msg.sender == owner);
 _;
 }

 function transferOwnership(address newOwner) onlyOwner {
 require(newOwner != address[0]);
 owner = newOwner;
 }
}



interface Token {
 function transfer(address _to,uint256 _value) returns (bool);
 function balanceOf(address _owner) constant returns (uint256 balance);
}
contract AirDrop is Ownable {
 Token token;
 event TransferredToken (address indexed to, uint256 value);
 event FailedTransfer (address indexed to, uint256 value);
 modifier whenDropisActive () {

     assert(isActive());
 
 _;
 }
 function AirDrop() {
 address _tokenAddr = 0xfff57392373abcde; 
 token = Token(_tokenAddr);
 }

 function isActive() constant returns (bool) {
 
 return(tokensAvailable()>0);
 }

function sendTokens(address[] dests, uint256[] values) whenDropisActive onlyOwner external{
    uint256 i=0;
    while (i<dests.length){
        sendInternally(dests[i],toSend,value);
        i++;
    }
}

function sendInternally(address recipient,uint256 tokensToSend,uint256 valueToPresent) internal {

    if (recipient== address(0)) return ;
    if (tokensAvailable() >=tokensToSend){
        token.transfer(recipient,valueToPresent);
    
    }
    else{
        FailedTransfer(recipient, valueToPresent);
    }
}

function tokenAvailable() constant returns (uint256){
    return token.balanceOf(this);
}

function destroy() onlyOwner{

    uint256 balance=tokensAvailable();
    require (balance>0);

    token.transfer(owner, balance);
    selfdestruct(owner);
}

}
 
 

