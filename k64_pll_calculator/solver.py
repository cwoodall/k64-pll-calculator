#!/usr/bin/env python
from z3 import *
from .util import solve_return_model

class PLLSolver(object):
    """
    Uses Z3 to solve for the PLL parameters described in the K64 datasheet:
    - http://cache.nxp.com/files/microcontrollers/doc/ref_manual/K64P144M120SF5RM.pdf

    Usage:
        fin = 24e6 # Hz
        desired_fout = 120e6 # Hz
        solver = PLLSolver()
        solver.solve(fin, desired_fout)
        print solver['d']
        print solver['m']
    """

    def __init__(self):
        """
        Initialize model and params.
        """
        self.params = {k: Int(k) for k in ['f_in', 'f_out', 'd', 'm']}
        self.model = None

    def __getitem__(self, k):
        """
        Get item from model.

        Will raise a TypeError error if model has not been generated yet.
        Will raise a KeyError if param is out of range

        Use after calling solve()

        @param self
        @param k the key to look up
        @return value of the key k after the model has been solved for
        """
        return self.model[self.params[k]]

    def serialize(self):
        if self.model:
            return {k: str(self.model[v]) for k,v in self.params.items()}
        else:
            return {}
    def solve(self, freq_in, freq_out=120e6, divide_range=(2e6, 4e6),
              d_range=(1, 25), m_range=(24, 55)):
        """
        Set up the constraints of our equation and then solve for them.

        @param freq_in Input frequency to the PLL in Hz
        @param freq_out Desired output frequency of the PLL in Hz
        @param divide_range Tuple of frequency range in Hz of the divide stage of the PLL (fin/d)
        @param d_range Valid values of d
        @param m_range Valid values of m

        @return None
        """
        facts = [
            # setup the equation which uses PRDIV (d) and VDIV (m)
            # This equation is set up from the K64 datasheet
            self.params['f_out'] == (self.params['f_in'] / self.params['d']) * self.params['m'],

            # From K64 datasheet page 589
            self.params['f_in'] / self.params['d'] >= divide_range[0],
            self.params['f_in'] / self.params['d'] <= divide_range[1],
            self.params['d'] >= d_range[0],  # From K64 datasheet page 589
            self.params['d'] <= d_range[1],
            self.params['m'] >= m_range[0],  # From K64 datasheet page 590
            self.params['m'] <= m_range[1],
            self.params['f_in'] == freq_in,
            self.params['f_out'] == freq_out]

        self.model = solve_return_model(facts)

        return self.model
    def __str__(self):
        """
        String representation of model
        """
        return str(self.model)
