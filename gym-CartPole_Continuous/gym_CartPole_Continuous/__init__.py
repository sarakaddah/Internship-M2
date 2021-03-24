#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gym.envs.registration import register

register(
    id='CartPole_Continuous-v1',
    entry_point='gym_CartPole_Continuous.envs:CartPole_Continuous',
    max_episode_steps=500,
)

register(
    id='CartPole_Continuous-v0',
    entry_point='gym_CartPole_Continuous.envs:CartPole_Continuous',
    max_episode_steps=200,
)
