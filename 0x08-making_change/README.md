## MAKING CHANGE PROBLEM
<strong>Making change problem</strong> in Python is all about the task of calculating the minimum number of coins or bills needed to represent a given amount of money(in this case total amount). This problem is often encountered in computer science and programming courses as an exercise in dynamic programming or greedy algorithms.
<br>
Several algorithms can be applied in solving the <em>Making Change Problem</em>:<br>
<ul>
<li>Dynamic Programming:<br> Dynamic programming is a popular approach for solving the making change problem. It involves breaking down the problem into smaller subproblems, solving them, and combining their solutions to find the optimal solution. The dynamic programming approach avoids redundant calculations by storing the results of subproblems in a table or memoization data structure. This technique can significantly improve the runtime of the solution.</li>
<br>
<li>Greedy Algorithm:<br> Greedy algorithms make locally optimal choices at each step with the hope of finding a globally optimal solution. In the making change problem, a greedy algorithm selects the largest denomination coin that can be used at each step until the desired amount is met. While the greedy algorithm doesn't always provide an optimal solution for all coin systems, it works well for some cases, such as the American coin system (quarters, dimes, nickels, and pennies).</li>
<br>
<li>Backtracking:<br> Backtracking is an algorithmic technique that explores all possible solutions by incrementally building a solution and undoing or backtracking when a dead-end or invalid solution is encountered. Backtracking can be used to exhaustively search through all combinations of coins to find the fewest number of coins needed to meet the target amount.</li>
<br>
<li>Integer Programming:<br> Integer programming is a mathematical optimization technique used to solve problems with integer variables and linear constraints. In the context of making change, an integer programming formulation can be used to determine the optimal combination of coins that minimizes the number of coins needed while satisfying the total amount constraint.</li>
<br>
<li>Branch and Bound:<br> Branch and bound is a technique used to solve optimization problems by systematically exploring the search space, pruning branches that are known to lead to suboptimal solutions. This technique can be applied to the making change problem to find the minimum number of coins needed by bounding the search space based on known optimal solutions.</li>
</ul>
<h2>CONCLUSION</h2>
<strong><em>Dynamic programming</em></strong> is a commonly used and effective approach for the making change problem it can significantly improve the runtime of the solution.
