from gameEnvironments import CardEnvironment

from tensorforce.agents import Agent
from tensorforce.execution import Runner
from tensorforce.environments import Environment


def main():
    environment = Environment.create(
        environment='gameEnvironments.CardEnvironment', max_episode_timesteps=None
    )

    agent = Agent.create(
        agent='ppo', environment=environment, batch_size=10, learning_rate=1e-3
    )

    # agent = Agent.create(agent='random', environment=environment)

    runner = Runner(agent=agent,
                    environment=environment,
                    max_episode_timesteps=None
                    )

    runner.run(num_episodes=2000)

    runner.run(num_episodes=1000, evaluation=True)

    runner.close()


if __name__ == '__main__':
    main()
