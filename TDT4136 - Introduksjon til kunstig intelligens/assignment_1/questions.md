# Assignment 1 - Håvard Hjelmeseth

## Define Artifical Intelligence

The term artifical intelligence was first used by John McCarthy, who stated that "It is the science and engineering of making intelligent machines, especially intelligent computer programs". But AI has no true definition, and the term is often used on systems that differ greatly in terms of complexity. The merriam webster dictionary defines AI to be "A branch of computer science dealing with the simulation of intelligent behavior in computers." and "The capability of a machine to imitate intelligent human behavior". Russel & Norvig mentions a few different definitions of AI, including "The study of how to make computers do things at which, at the moment, people are better." (Rich and Knight, 1991). My personal favorite is "(AI is) the study of the computations that make it possible to perceive, reason and act" (Winston, 1992).

## What is the turing test, and how is it conducted?

The turing test is named after Alan Turing, and is a test to see if a computer can act intelligently. The test is conducted by someone communication with a computer or a human using only a screen and a keyboard, and the test is considered a success if the tester can't tell if they are communication with a computer or a human being.

## What is the relationship between thinking rationally and acting rationally? Is rational thinking an absolute condition for acting rationally?

One would be led to belive that to act rationally one must first think rationally, but this is not always the case. There are problems that do require rational thinking to solve, but there are also problem that are far to complex to be solved with rational thinking. For some problems an agent acting fast might be more rational than solving the problem with rational thinking. The textboox mentions a good example, the humans ability to recoil from a hot stove which is a rational action caused by human reflexes, and not the result of thinking rationally. Rational thinking is not an absolute condition for acting rationally.

## Describe rationality. How is it defined?

Rationality is making the correct choices which will lead to the most prefferable outcome. Acting rationally is not guaranteed to give the best outcome, but it is the action that we consider most likely to give the best outcome. The textbook defines a rational agent as "For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.

## What is Aristotle’s argument about the connection between knowledge and action? Does he make any further suggestion that could be used to implement his idea in AI? Who was/were the first AI researcher(s) to implement these ideas? What is the name of the program/system they developed? Google about this system and write a short description about it.

Aristotle argued that actions are justified by a logical connection between goals and knowledge of the action's outcome. Furthe he suggests an algorith that could be used to implement his idea, stating that we should assume the end and rather consider the means to get to that end. 2300 years later, his algorithm was implemented by Newell and Simon in their General problem solver. The general problem solver was a computer program written in 1959 with the intention to work as a universal problem solver machine. It was supposed to be able to solve any problem that could be expressed as a set of well formed formulas.

## Consider a robot whose task it is to cross the road. Its action portfolio looks like this: look-back, lookforward, look-left-look-right, go-forward, go-back, go-left and go-right

### While crossing the road, a helicopter falls down on the robot and smashes it. Is the robot rational?

We cannot exclude the robot being rational in this situation, such an outcome is not within reasonable expectations, and the robot can only act on the information it has.

### While crossing the road on a green light, a passing car crashes into the robot, preventing it from crossing. Is the robot rational?

Again the robot did not perform an irrational action as the passing car must have driven on a red light, as such the robot could not have expected the outcome with the information it had.

## Consider the vacuum cleaner world described in Chapter 2.2.1 of the textbook. Let us modify this vacuum environment so that the agent is penalized 1 point for each movement

### Can a simple reflex agent be rational for this environment? Explain your answer

A simple reflex agent in the vacuum cleaner world described in Chapter 2.2.1 can not be rational if the agent is penalized 1 point for each movement. As the agent has no state, it would oscilate between the two squares after they are both clean, wasting points.

### Can a reflex agent with state be rational in this environment? Explain your answer.

If the agent has a state it can remember that is has already cleaned both of the squares, and does not have to oscilate back and forth between clean squares. Such an agent would be rational.

### Assume now that the simple reflex agent (i.e., no internal state) can perceive the clean/dirty status of both locations at the same time. Can this agent be rational? Explain your answer. In case it can be rational, design the agent function.

If the simple reflex agent can perceive the clean/dirty state of both locations at the same time, it would not need to keep state to be rational. The agent could clean both squares, and keep checking the status of both squares, without having to move. This agent would be rational.

## Consider the vacuum cleaner environment shown in Figure 2.3 in the textbook. Describe the environment using properties from Chapter 2.3.2, e.g. episodic/sequential, deterministic/stochastic etc. Explain selected values for properties in regards to the vacuum cleaner environment.

The described vacuum cleaner environment is partially observable, as the vacuum cleaner can only observe the cleanliness of the square it is on. The environment would also be a single-agent environment, as only the one cleaning agent is present. When it comes to the question of deterministic vs stochastic it is not as clear. The squares might become dirty again after the agent has cleaned them, therefore the environment cannot be fully deterministic. The described environment is also sequential, as the cleaning agent will try to avoid cleaning squares that are already clean.

## Discuss the advantages and limitations of these four basic kinds of agents:

### Simple reflex agents

Simple reflex agents have the advantage that they are simple and relatively cheap to produce. They act only based on the current percept, and are therefore limited in the kind of descision making they can perform.

### Model-based reflex agents

A model based reflex agent maintains an internal state, keeping track of the part of the world that it cannot sense. This is useful for making descisions not only based on current percept, but also previous percept. Some drawbacks compared to simple reflex agents are complexity in terms of production and implementation, and also the matter of price.

### Goal-based agents

Goal based agents also take into account the goal that it is trying to get to. Doing this, it can consider possible actions and choose the one leading to the goal. These descisions differ greatly in terms of complexity. The goal based agent can be less efficient than simpler agents, but are more flexible as the knowledge that supports its descision is represented explicitly and can be modified.

### Utility-based agents

Utility based agents are similar to goal based agents, but also takes the "utility" of the choices into account. For example a goal based GPS agent might find a route to the desired destination, but an utility based GPS agent will try to find the shortest or cheapest path, or any path that maximizes its performance rating. Utility based agents are far greater in complexity in terms of producing and implementing.
