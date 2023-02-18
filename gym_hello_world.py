import gym
env = gym.make("CarRacing-v1", domain_randomize=True)
env.action_space.seed(42)

observation, info = env.reset(seed=6)

for _ in range(10000):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

    if terminated or truncated:
        observation, info = env.reset()

env.close()