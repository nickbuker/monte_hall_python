import numpy as np

def monte_hall(switch_door, n_sim=10000):
    """ Simulates the Monte Hall problem to find the probability of winning
    by either the strategy of keeping the original guess or switching doors

    Parameters
    ----------
    switch_door : bool
        whether or not to switch doors after being shown a door
    n_sim : int
        number of simulations to run

    Returns
    -------
    float
        proportion of games won
    """
    return _run_sims(switch_door, n_sim)


def _run_sims(switch_door, n_sim):
    """ Runs the simulation n_sim times and returns the mean outcome (prop games won)

    Parameters
    ----------
    switch_door : bool
        whether or not to switch doors after being shown a door
    n_sim : int
        number of simulations to run

    Returns
    -------
    float
        proportion of games one
    """
    doors = np.array([0, 0, 1])
    results = []
    for _ in range(n_sim):
        results.append(_play_game(switch_door, doors))
    return np.mean(results)


def _play_game(switch_door, doors):
    """ Runs an individual game

    Parameters
    ----------
    switch_door : bool
        whether or not to switch doors after being shown a door
    doors : numpy array
        array with 3 elements (two zeroes and a one) corresponding to
        wins or loss

    Returns
    -------
    int
        0 for loss or 1 for victory in the game

    """
    np.random.shuffle(doors)
    if switch_door:
        if doors[1] == 0:
            return doors[2]
        if doors[2] == 0:
            return doors[1]
    else:
        return doors[0]

