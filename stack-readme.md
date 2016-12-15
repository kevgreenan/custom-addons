| Function            | Description                                                                                       |
| ------------------- |--------------------------------------------------------------------------------------------------:|
| Stack(&lt;int&gt;)        | Declares an instance of the stack with size &lt;int&gt;                                                 |
| Clear()             | Clears the stack by reseting the index                                                            |
| Contains(&lt;object&gt;)  | Returns True if stack contains &lt;object&gt;, otherwise False                                          |
| Count()             | Returns the number of items on the stack; NOT the size                                            |
| IncreaseSize()      | NOT A USER FUNCTION: this will append the stack based on the current size; it is called by Push() |
| IsEmpty()           | Returns True if stack is empty, False if 1+ items                                                 |
| Peek()              | Returns the item on the top of the stack without popping                                          |
| PeekNext()          | Returns the second item on the stack without popping                                              |
| Pop()               | Returns and removes the top of the stack                                                          |
| Purge(&lt;int&gt;)        | Clears the stack and resizes it to &lt;int&gt;                                                          |
| Push(&lt;object&gt;)      | Adds &lt;object&gt; to the top of the stack                                                             |
| RemoveAll(&lt;object&gt;) | Removes ALL OCCURRENCES, regardless of order, of &lt;object&gt; from the stack                          |
| ToString()          | Outputs the contents of the stack to a string                                                     |
