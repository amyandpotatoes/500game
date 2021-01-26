from gameEnvironments import CardEnvironment

from tensorforce.agents import Agent
from tensorforce.execution import Runner

def main():
    environment = CardEnvironment()
    agent = Agent.create(
        agent='ppo', environment=environment, batch_size=10, learning_rate=1e-3
    )
    runner = Runner(agent=agent,
        environment=environment,
        max_episode_timesteps=500
    )

    runner.run(num_episodes=200)

    runner.run(num_episodes=100, evaluation=True)

    runner.close()

if __name__ == '__main__':
    main()
