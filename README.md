# elo_game
A small game that allows the user to input and track their elo rating alongside simulated matches against other elo brackets.

The expected score $E_A$ of player A is based on the formula:

$$
E_A = \frac{1}{1 + 10^{(R_B - R_A)/400}}
$$

Where player A has an elo rating of $R_A$. This can be used to calculate the *percent chance of a win*. Consequently, $E_B$ is derived from the formula:

$$
E_B = \frac{1}{1 + 10^{(R_A - R_B)/400}}
$$

--------------------------

To update the score of player A (usually done after a match), the formula is:

$$
R'_A = R_A + K \cdot (S_A - E_A)
$$

Where $R'_A$ is the updated score of player A and $S_A$ is the actual outcome (e.g. 0 for loss, 0.5 for draw, 1 for win.). $K$ is a scaling factor which controls the amount of gain or loss per update. For example, in GM chess tournaments a smaller $K$-factor of 10 is used to ensure ratings don't fluctuate rapidly. In more casual online chess websites, $K = 32$ has become the standard. When a new player makes an online chess account (or in other uncertain situations), a $K$-factor of 50+ might be used temporarily to ensure their elo rating reaches their skill-level quickly.

Many iterations of the elo rating system has been implemented in almost every competetively-ranked game, video game, and sport.

# Instructions
Run the elo_game.py through command line

No AI was used creating this
