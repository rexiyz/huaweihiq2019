import math
import random
import sys
from projectq import MainEngine
from projectq.ops import H, Z, X, Measure, All
from projectq.meta import Loop, Compute, Uncompute, Control

from mpi4py import MPI


def run_grover(eng, n, oracle, expected):
    """
    Runs Grover's algorithm on n qubit using the provided quantum oracle.

    Args:
        eng (MainEngine): Main compiler engine to run Grover on.
        n (int): Number of bits in the solution.
        oracle (function): Function accepting the engine, an n-qubit register,
            and an output qubit which is flipped by the oracle for the correct
            bit string.

    Returns:
        solution (list<int>): Solution bit-string.
    """
    oracle_out = eng.allocate_qubit()
    x = eng.allocate_qureg(n)

    # start in uniform superposition
    All(H) | x

    # number of iterations we have to run:
    num_it = int(math.pi/4.*math.sqrt(1 << n))
    print("number of Grover iterations: ", num_it)

    # prepare the oracle output qubit (the one that is flipped to indicate the
    # solution. start in state 1/sqrt(2) * (|0> - |1>) s.t. a bit-flip turns
    # into a (-1)-phase.
    
    X | oracle_out
    H | oracle_out

    # run num_it iterations
    with Loop(eng, num_it):
        # oracle adds a (-1)-phase to the solution
        oracle(eng, x, oracle_out, expected)

        # reflection across uniform superposition
        with Compute(eng):
            All(H) | x
            All(X) | x

        with Control(eng, x[0:-1]):
            Z | x[-1]

        Uncompute(eng)

    Measure | x
    Measure | oracle_out

    eng.flush()
    # return result
    return [int(qubit) for qubit in x]


        
def oracle(eng, qubits, output, expected):
    
    """
    Args:
        eng (MainEngine): Main compiler engine the algorithm is being run on.
        qubits (Qureg): n-qubit quantum register Grover search is run on.
        output (Qubit): Output qubit to flip in order to mark the solution
        expected - bit-string solution.
    """
    qubits1 = [qubits[elem[0]] for elem in enumerate(expected) if elem[1]==0 ]
    
    with Compute(eng):
        All(X) | qubits1
    with Control(eng, qubits):
        X | output
    Uncompute(eng)        



if __name__ == "__main__":
    
    print("=====================================================================")
    print("= This is the Grover algorithm with arbitrary oracle demo")
    n = 8
    print('Size of register: ', n)
    Nmax = (1 << n) - 1
    N = 100
    print("Expected value in the range from 0 to {}: ".format(Nmax), N ) 
    expected = [int(i) for i in "{0:b}".format(N)]
    expected =([0 for i in range(n - len(expected))]+expected)
    print("Expected binary: ", expected)
       
    eng = MainEngine() 
        
    # run Grover search 
    found = run_grover(eng, n, oracle, expected)
    int_found = int(sum([found[i]*(1 << (n-i-1)) for i in range(n)]))
    print("found: ", found, int_found)
    print("=====================================================================")
