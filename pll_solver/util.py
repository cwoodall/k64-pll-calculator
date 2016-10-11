#!/usr/bin/env python
from z3 import *
import logging
logger = logging.getLogger(__name__)

def solve_return_model(fact_list):
    """
    The default z3.solve() method prints to the screen. This uses the basis of
    that function to take a list of facts, add it to a solver and then return
    a z3 model with a solution.

    Relies on exceptions raised by calling s.mode() on an invalid model.

    @param a list of z3 facts and constraints
    @return A valid z3 model
    @raises Z3Exception
    """
    s = Solver()
    s.add(*fact_list)
    r = s.check()
    if r == unsat:
        logger.critical("no solution")
    elif r == unknown:
        logger.critical("failed to solve")

    return s.model()
