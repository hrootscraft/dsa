LL is a form of sequential collection which is stored in heap (dynamic) memory.

Made of independent nodes that may contain different types of data.

A head node points to the first node and the 1st one points to next... 

The last node is pointed to by tail node (optional-might be done for easy access of last item) 
and last node points to null.

Dynamic sizing can be done on LL; no need to specify it's size initially.

<br>
<br>
Arrays Vs. LL

1. A-Indexed, Contiguous 
2. L-No indices, not contiguous
 
<br>
Types of LL:

1. Singly LL            |   head -> node_1 -> ... node_n -> null        |  
2. Circular LL          |   head -> node_1 -> ... node_n -> head        |  eg. in chess game of 4 players, after the controller is 
                        |                                               |  done making a round from 1 to 4 it again has to go to make 
                        |                                               |  that round ie go from 4th player to 1st, 
                        |                                               |  for this control logic we might use circular LL
3. Doubly LL            |   each node has reference of previous         |  eg. songs on spotify can be skipped backward & forward
                        |   and next node, last node points to null     |  
4. Circular Doubly LL   |   doubly LL with last node pointing to 1st    |  eg. when you tap alt+cmd, we can traverse the array of applications back & forth