# Q3 – UGV Navigation in Dynamic Obstacle Environment

## Problem Description

In the previous problem, obstacles were assumed to be **static and known beforehand**.  
However, in real-world environments obstacles may be **dynamic**, meaning they can appear or move while the robot is navigating.

Therefore, the **Unmanned Ground Vehicle (UGV)** must be able to **detect obstacles during navigation and replan its path dynamically** to reach the goal safely.

---

## Approach

The UGV navigation system follows a **Sense–Plan–Act loop**.

1. The robot first computes an initial shortest path using the **A\*** search algorithm.
2. While moving toward the goal, the robot continuously **senses the environment** using simulated sensors.
3. If a **new obstacle is detected**, the grid map is updated.
4. The robot **recomputes the shortest path** from its current position to the goal.
5. This process continues until the robot reaches the goal.

This strategy allows the robot to **adapt to environmental changes** and still navigate efficiently.

---

## Algorithm Used

To handle dynamic environments efficiently, the system uses **Repeated A\*** search.

Repeated A\* works by recomputing the optimal path whenever the environment changes.  
If a new obstacle appears while the robot is navigating, the robot updates the map and runs **A\*** again from its **current position to the goal**.

This ensures the UGV always follows the **optimal path based on the most recent map information**.

Other algorithms commonly used for dynamic path planning include:

- **D\*** (Dynamic A\*)
- **D\* Lite**
- **Real-Time A\***

In this implementation we simulate the behaviour using **Repeated A\***.

---

## Pseudocode

```text
Initialize grid map
Set Start node and Goal node

Compute initial shortest path using A*

WHILE robot has not reached the goal DO

    Move one step along the planned path

    Sense the environment

    IF a new obstacle is detected THEN
        Update the grid map
        Recompute path from current position using A*
    END IF

END WHILE

Goal reached
```

---

## Measures of Effectiveness

To evaluate the navigation performance, the following metrics are used:

- **Path Length** – total number of steps taken to reach the goal  
- **Execution Time** – time required to compute paths  
- **Nodes Expanded** – number of explored states during search  
- **Number of Replans** – how many times the robot recomputed the path  
- **Mission Success Rate** – whether the robot successfully reaches the goal  

---

## Conclusion

In dynamic environments, the UGV cannot rely on a fixed path because obstacles may appear unexpectedly.  
By continuously sensing the environment and **replanning paths using algorithms such as Repeated A\***, the robot can safely navigate toward the goal while avoiding newly discovered obstacles.

This approach ensures that the UGV can **adapt to changes in the environment and still compute an optimal path to the destination**.
