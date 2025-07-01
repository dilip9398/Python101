## Turtle Race

This project simulates a *simple turtle race* on a screen.
It **sets up** multiple turtles with different colors,
**asks the user** to bet on which color will win,
then **runs the race** by moving each turtle forward randomly.
Finally, it **announces the winner** and whether the user's bet was correct.


## Visual Overview

```mermaid
flowchart TD
    A0["The Race Screen
"]
    A1["Race Participant (Turtle)
"]
    A2["Race Setup
"]
    A3["User Betting
"]
    A4["Race Engine (Movement Loop)
"]
    A5["Race Conclusion and Result
"]
    A2 -- "Configures" --> A0
    A2 -- "Creates" --> A1
    A3 -- "Gets input from" --> A0
    A3 -- "Starts/Stops" --> A4
    A4 -- "Moves" --> A1
    A5 -- "Checks state of" --> A1
    A5 -- "Compares with bet" --> A3
    A5 -- "Stops" --> A4
```


