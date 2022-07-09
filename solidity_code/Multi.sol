pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

contract  Mutli{
    uint public peopleCount=0;
    mapping (address =>Player ) public players;

    enum Level {Novice, Intermediate, Advanced}


     struct  Player {

        address  playerAddress;
         Level playerLevel;
        string firstName;
         string lastName;
        uint createdTime;
    }
    function addPlayer (string memory firstName, string memory lastName) public returns(Player memory) {

   
         players[msg.sender]=Player(msg.sender, Level.Novice, firstName, lastName, block.timestamp);
         return players[msg.sender];
    }
    function getPlayerLevel(address playerAddress) public view returns(Level) {
         Player storage player= players[playerAddress];
         return player.playerLevel;
    }
    function changePlayerLevel (address playerAddress) public{
         Player storage player=players[playerAddress];

         if (block.timestamp>=player.createdTime+20)
         {
             player.playerLevel=Level. Intermediate;

         }
    }
}