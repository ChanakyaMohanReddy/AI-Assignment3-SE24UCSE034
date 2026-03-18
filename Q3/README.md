# Q3 – UGV Navigation in Dynamic Obstacle Environment

## Problem Description

In the previous problem, obstacles were assumed to be static and known beforehand.
However, in real-world environments obstacles may be dynamic, meaning they can appear or move while the robot is navigating.

Therefore, the Unmanned Ground Vehicle (UGV) must be able to detect obstacles during navigation and replan its path dynamically to reach the goal safely.

### Approach

The UGV uses a Sense–Plan–Act loop:

The robot first computes an initial shortest path using A*.

While moving toward the goal, the robot continuously senses the environment using onboard sensors.

If a new obstacle is detected, the map is updated.

The robot recomputes the path from its current position to the goal.

This process continues until the robot reaches the goal.

This approach is known as Dynamic Replanning.


### Algorithms commonly used for this include:

D* (Dynamic A*)

D* Lite

Repeated A*

In this implementation we simulate the behaviour using Repeated A*.

## Pseudocode

Initialize grid map
Set Start and Goal nodes

Compute initial path using A*

while robot has not reached the goal

    Move one step along the planned path

    Sense the environment

    if a new obstacle is detected then
        Update the grid map
        Recompute path from current position using A*
    end if

end while

Goal reached

## Measures of Effectiveness

To evaluate the navigation performance, the following metrics are used:

Path Length – total number of steps taken to reach the goal

Execution Time – time required to compute paths

Nodes Expanded – number of explored states during search

Number of Replans – how many times the robot had to recompute the path

Mission Success Rate – whether the robot successfully reaches the goal


## Conclusion

In dynamic environments, the UGV cannot rely on a fixed path because obstacles may appear unexpectedly.
By continuously sensing the environment and replanning paths using algorithms such as D* Lite or Repeated A*, 
the robot can safely navigate toward the goal while avoiding newly discovered obstacles.
