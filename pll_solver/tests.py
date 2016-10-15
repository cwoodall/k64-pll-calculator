from pll_solver import PLLSolver
from pll_solver.scripts.cli import get_verbosity_level
from unittest import TestCase
from z3 import *


class TestCLI(TestCase):
    def test_get_verbosity_level(self):
        import logging
        assert (get_verbosity_level(0) == logging.CRITICAL)
        assert (get_verbosity_level(1) == logging.ERROR)
        assert (get_verbosity_level(2) == logging.WARNING)
        assert (get_verbosity_level(3) == logging.INFO)
        assert (get_verbosity_level(4) == logging.DEBUG)
        assert (get_verbosity_level(5) == logging.NOTSET)

class TestPLLSolver(TestCase):
    def setUp(self):
        self.p = PLLSolver()

    def test_pll_init(self):
        assert self.p.model == None
        assert len(self.p.params.keys()) == 4
        params = ['f_in', 'f_out', 'm', 'd']
        for param in params:
            assert param in self.p.params.keys()

    def test_pll_except_on_get_with_invalid_param(self):
        try:
            self.p['i']
        except KeyError as e:
            assert e
            return
        assert None

    def test_pll_unsolved_model_access(self):
        try:
            self.p['m']
        except TypeError as e:
            assert e
            return
        assert None

    def test_pll_solver_returns_model_string(self):
        assert str(self.p) == str(None)
        assert self.p.solve(24e6, 120e6) == self.p.model
        assert self.p.model != None
        assert str(self.p) == str(self.p.model)

    def test_pll_solver_works_on_known_solution(self):
        self.p.solve(24e6, 120e6)
        assert self.p['d'] == 6
        assert self.p['m'] == 30
        assert self.p['f_in'] == 24e6
        assert self.p['f_out'] == 120e6

    def test_pll_solver_serialize(self):
        assert self.p.serialize() == {}
        self.p.solve(24e6, 120e6)
        self.p.serialize() == {
            "d": str(6),
            "m": str(30),
            "f_in": str(int(24e6)),
            "f_out": str(int(120e6))
        }
    def test_pll_solver_impossible_solution(self):
        try:
            self.p.solve(24e6, -1)
        except Z3Exception as e:
            assert e
            return
        assert None
