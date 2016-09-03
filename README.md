# Prioritized Experience Replay

### Usage
1. in rank_base.py Experience.stroe give a simple description of store replay memory, or you can also refer rank_base_test.py
2. It's more convenient to store replay as format (state_1, action_1, reward, state_2, terminal). If we use this method, all replay memory in Experience are legal and can be sampled as we like.

### Rank-based
use binary heap tree as priority queue, and build an Experience class to store and retrieve the sample

### Proportional
not implement yet

### Reference
1. "Prioritized Experience Replay" http://arxiv.org/abs/1511.05952
2. [Atari](https://github.com/Kaixhin/Atari) by @Kaixhin, Atari uses torch to implement rank-based algorithm.

### Application
1. TEST1 PASSED: These code has been applied to my own NLP DQN experiment, it significantly improves performance.
