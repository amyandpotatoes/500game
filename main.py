# just using template from FLight example
# will make it work for cards
# scaffold, not a working python file at this point
from game-environments import CardEnvironment

def run(environment, agent, n_episodes, max_step_per_episode, test=False):
    """
    Train agent for n_episodes
    """
    environment.FlightModel.max_step_per_episode = max_step_per_episode
    # Loop over episodes
    for i in range(n_episodes):
        # Initialize episode
        episode_length = 0
        states = environment.reset()
        internals = agent.initial_internals()
        terminal = False
        while not terminal:
            # Run episode
            episode_length += 1
            actions = agent.act(states=states)
            states, terminal, reward = environment.execute(actions=actions)
            agent.observe(terminal=terminal, reward=reward)

    # return the 'score' for recording purposes
    return environment.FlightModel.Pos[0]


def runner(
    environment,
    agent,
    max_step_per_episode,
    n_episodes,
    n_episodes_test=1,
    combination=1,
):
    # Train agent
    result_vec = [] #initialize the result list
    for i in range(round(n_episodes / 100)): #Divide the number of episodes into batches of 100 episodes
        if result_vec:
            print("batch {} Best result={}".format(i, result_vec[-1])) #Show the results for the current batch
        # Train Agent for 100 episode
        run(environment, agent, 100, max_step_per_episode)
        # Test Agent for this batch
        test_results = run(environment, agent, n_episodes_test, max_step_per_episode, test=True)
        # Append the results for this batch
        result_vec.append(test_results)

    # Plot the evolution of the agent over the batches
    plot_multiple(
        Series=[result_vec],
        labels = ["Reward"],
        xlabel = "episodes",
        ylabel = "Reward",
        title = "Reward vs episodes",
        save_fig=True,
        path="env",
        folder=str(combination),
        time=False,
    )
    # Terminate the agent and the environment
    agent.close()
    environment.close()

def main:
    # Instantiane our environment
    environment = CardEnvironment()
    # Instantiate a Tensorforce agent
    agent = Agent.create(agent="ppo",environment=environment)

    # Call runner
    runner(environment, agent, max_step_per_episode=1000, n_episodes=10000)

if __name__ == '__main__':
    main()