LL is a form of sequential collection which is stored in heap (dynamic) memory.

Made of independent nodes that may contain different types of data.

A head node points to the first node and the 1st one points to next... 

The last node is pointed to by tail node (optional-might be done for easy access of last item) 
and last node points to null.

Dynamic sizing can be done on LL; no need to specify it's size initially.

<br>
<br>
Arrays Vs. LL

| Property      | Array (A)                      | Linked List (L)                                        |
| ------------- | ------------------------------ | ------------------------------------------------------ |
| Indexing      | Direct/random access via index | No direct indices (must traverse)                      |
| Memory layout | Contiguous block in memory     | Nodes stored non-contiguously, connected with pointers |
| Resizing      | Fixed size once created        | Dynamic sizing – can grow/shrink at run-time           |

 
<br>
Types of LL:

| # | Type                   | Pointer / Structure Pattern                                        | Everyday Analogy / Use-Case                                                                       |
| - | ---------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| 1 | **Singly LL**          | `head → node₁ → … → nodeₙ → null`                                  | –                                                                                                 |
| 2 | **Circular LL**        | `head → node₁ → … → nodeₙ → head`                                  | Turn-based games (e.g., 4-player chess): after the 4th player acts, control loops back to the 1st |
| 3 | **Doubly LL**          | Each node stores `prev` and `next`; last node’s `next → null`      | Music apps like Spotify – skip tracks forward **and** backward                                    |
| 4 | **Circular Doubly LL** | Doubly LL where last node’s `next → head` and head’s `prev → last` | Alt + Tab / Cmd + Tab application switcher: cycle through open apps in both directions            |
