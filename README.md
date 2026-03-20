# Monte-Carlo-Analysis

Let's perform a Monte Carlo analysis to study the [Buffon needle problem](https://en.wikipedia.org/wiki/Buffon's_needle_problem). The problem is thus: suppose your floor is made of floor boards, and each board has a width t
. If you have a needle, of length ℓ
, and you randomly drop it onto the floor, what is the probability that the needle will land on one of the edges of the boards?

As it turns out, this problem can be solved exactly, as you can see by following the above link. We will perform a Monte Carlo anlysis of this problem to see if these predictions are correct. We will do this by assuming that, for a single throw of the needle, the centre of the needle, x
, can be located anywhere between the one edge of the boards and the centre: 0≤x≤t2
 (the symmetry of the problem means we only need to look at half the width). Similarly, the angle of the needle relative to the edge of the board, θ
, can range from 0≤θ≤π2
, where θ=0
 is parallel to the edge of the board.
