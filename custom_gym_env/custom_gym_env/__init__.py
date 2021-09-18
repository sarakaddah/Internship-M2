from gym.envs.registration import register

register(
    id='My_MountainCar-v0',
    entry_point='custom_gym_env.envs:My_MountainCar_env',
    reward_threshold=-110.0,
    max_episode_steps=200,
)

