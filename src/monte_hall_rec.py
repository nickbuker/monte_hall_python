import numpy as np

def monte_hall_rec(switch_door, n_sim=500):
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
    doors = np.array([0, 0, 1])
    results = []

    def _play_game(switch_door, n_sim, doors, i=0):
        """ Runs the simulation n_sim times appending the outcomes to results

        Parameters
        ----------
        switch_door : bool
            whether or not to switch doors after being shown a door
        n_sim : int
            number of simulations to run
        doors : numpy array
            array with 3 elements (two zeroes and a one) corresponding to wins or losses
        i : int
            iterator that tracks the number of games run

        Returns
        -------
        None
        """
        if i == n_sim:
            return
        else:
            np.random.shuffle(doors)
            if switch_door:
                if doors[1] == 0:
                    results.append(doors[2])
                else:
                    results.append(doors[1])
            else:
                results.append(doors[0])
        i += 1
        _play_game(switch_door, n_sim, doors, i)

    _play_game(switch_door,n_sim, doors)
    return np.mean(results)