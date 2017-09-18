import numpy as np

def monte_hall(switch_door, n_sim=10000):
    """

    Parameters
    ----------
    switch_door
    n_sim

    Returns
    -------
    float
        proportion of games won
    """
    return _run_sims(switch_door, n_sim)


def _run_sims(switch_door, n_sim):
    """

    Parameters
    ----------
    swich_door
    n_sim

    Returns
    -------

    """
    doors = np.array([0, 0, 1])
    results = []
    for _ in range(n_sim):
        results.append(_play_game(switch_door, doors))
    return np.mean(results)


def _play_game(switch_door, doors):
    np.random.shuffle(doors)
    if switch_door:
        if doors[1] == 0:
            return doors[2]
        if doors[2] == 0:
            return doors[1]
    else:
        return doors[0]

