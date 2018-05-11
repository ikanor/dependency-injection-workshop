from doublex import *
from expects import *
from doublex_expects import *

import doctest

import playground

from playground import factorial

with description('Basic tests'):

    with context('Doc Tests'):

        with it('runs ok'):
            failed, tested = doctest.testmod(playground)
            expect(failed).to(equal(0))

    with context('Factorial basics'):

        with it('computes factorial'):
            expect(factorial(0)).to(be(1))
            expect(factorial(1)).to(be(1))
            expect(factorial(3)).to(be(6))
            expect(factorial(5)).to(be(120))
