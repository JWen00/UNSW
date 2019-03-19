# Hunter 
#### Information that the Hunter Knows.. 
  1. Whether the Dracula is at Sea or Land 
    * Can use this to figure out which sea he is in.. or the fact that Dracula is near a port 
  2. The position of the trail if Hunter arrives in a city which Dracula's trail is in (Correct me if I'm wrong) 
  3. That Dracula has passed the city if he encounters a TRAP or VAMPIRE. 
  4. The position of the trail the Dracula has DOUBLE_BACK'ed to in the last move
  5. The fact that a Dracula's last move was HIDE


### Todo list: 
  * Setup a way of communication between Hunters (If necessary)   
  * Setup a struct which can store information about all past encounters.. ?   
  * Setup a function which tries to determine which Sea/Port the Dracula is at   
  * See if Players are camping CD, if they are, play the chicken game 
    
### Proposals
#### Proposal 2:
  Round 0 Strategy: Scatter around the map -> as previous 
  Round 6 strategy: If dracula has not been spotted, all Hunters to rest 
  
  If a Hunter reaches <6HP, then rest for the turn (Ecounter + Trap deals 6dmg) 

#### Proposal 1: 
  
  Strategy - To counter Dracula as much as possible by tracking down his location 
  1. Have 1 HUNTER Stay near   
  {CASTLE_DRACULA, GALATZ, KLAUSENBURG, BUCHAREST, CONSTANTA, SZEGED} 
  2. Have 1 HUNTER Traverse around ports surrounding  
  {NORTH_SEA, IRISH_SEA, ENGLISH_CHANNEL, ATLANTIC_OCEAN, BAY_OF_BISCAY} 
  3. Have 1 HUNTER Traverse around ports surrounding  
  {MEDITERRANEAN_SEA, TYRRHENIAN_SEA, IONIAN_SEA, BLACK_SEA} 
  4. Have 1 HUNTER Traverse around main cities so that when they get information they can then head towards the direction of another hunter. 
  

  
  
  # Dracula 
  
  Strategy: 
  Spawn at CASTLE_DRACULA (if safe) then HI or BD back to gain health one he hits <15HP
 
