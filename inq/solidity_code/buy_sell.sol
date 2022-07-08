pragma solidity ^0.6.0;
contract ERC20Basic{
 uint256 public constant tokenPrice = 5; // 1 token for 5 wei
 
 function buy(uint256 _amount) external payable {
 // e.g. the buyer wants 100 tokens, needs to send 500 wei
 require(msg.value == _amount * tokenPrice, 'Need to send exact amount of wei');
 
 /*
 * sends the requested amount of tokens
 * from this contract address
 * to the buyer
 */
 transfer(msg.sender, _amount);
 }
 
 function sell(uint256 _amount) external {
 // decrement the token balance of the seller
 balances[msg.sender] -= _amount;
// increment the token balance of this contract
 balances[address(this)] += _amount;

 // e.g. the user is selling 100 tokens, send them 500 wei
 payable(msg.sender).transfer(_amount * tokenPrice);


 }
}