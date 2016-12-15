##LIST OF FUNCTIONS:

| Function            | Description                                                                                       |
| ------------------- |--------------------------------------------------------------------------------------------------:|
| Stack(<int>)        | Declares an instance of the stack with size <int>                                                 |
| Clear()             | Clears the stack by reseting the index                                                            |
| Contains(<object>)  | Returns True if stack contains <object>, otherwise False                                          |
| Count()             | Returns the number of items on the stack; NOT the size                                            |
| IncreaseSize()      | NOT A USER FUNCTION: this will append the stack based on the current size; it is called by Push() |
| IsEmpty()           | Returns True if stack is empty, False if 1+ items                                                 |
| Peek()              | Returns the item on the top of the stack without popping                                          |
| PeekNext()          | Returns the second item on the stack without popping                                              |
| Pop()               | Returns and removes the top of the stack                                                          |
| Purge(<int>)        | Clears the stack and resizes it to <int>                                                          |
| Push(<object>)      | Adds <object> to the top of the stack                                                             |
| RemoveAll(<object>) | Removes ALL OCCURRENCES, regardless of order, of <object> from the stack                          |
| ToString()          | Outputs the contents of the stack to a string                                                     |
