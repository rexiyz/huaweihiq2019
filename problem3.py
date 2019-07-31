# File name: problem3.py
import math
from projectq import MainEngine
from projectq.ops import X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, Measure, All
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.cengines import (MainEngine,
	AutoReplacer,
	LocalOptimizer,
	TagRemover,
	InstructionFilter,
	DecompositionRuleSet)
import projectq.setups.decompositions
from hiq.projectq.backends import SimulatorMPI
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from mpi4py import MPI
def run_circuit(qureg, theta):
	"""
	Runs target circuit using the theta.
	Args:
		qureg (allocate_qureg):Assigned qubit register
		theta: Parameters that need to be optimized.
	Returns:
		None.
	"""
	X | qureg[0]
	X | qureg[1]
	X | qureg[2]
	X | qureg[3]
	X | qureg[4]
	X | qureg[5]
	X | qureg[6]
	X | qureg[7]
	X | qureg[8]
	X | qureg[9]
	Rx(theta[0]) | qureg[0]
	H | qureg[5]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[10]
	H | qureg[5]
	Rx(theta[2]) | qureg[0]
	H | qureg[6]
	H | qureg[7]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[6], qureg[7] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	H | qureg[7]
	H | qureg[6]
	Rx(theta[0]) | qureg[3]
	H | qureg[4]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[10]
	H | qureg[4]
	Rx(theta[2]) | qureg[3]
	Rx(theta[0]) | qureg[0]
	H | qureg[10]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	Rz(theta[0]) | qureg[10]
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[10]
	Rx(theta[2]) | qureg[0]
	H | qureg[0]
	H | qureg[1]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	H | qureg[1]
	H | qureg[0]
	Rx(theta[0]) | qureg[8]
	Rx(theta[0]) | qureg[9]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[0]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[9]
	Rx(theta[2]) | qureg[8]
	Rx(theta[0]) | qureg[2]
	H | qureg[5]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[11]
	H | qureg[5]
	Rx(theta[2]) | qureg[2]
	H | qureg[8]
	H | qureg[9]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[9]
	H | qureg[8]
	H | qureg[2]
	H | qureg[3]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[1]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[3]
	H | qureg[2]
	Rx(theta[0]) | qureg[8]
	H | qureg[9]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[8], qureg[9] )
	H | qureg[13]
	H | qureg[12]
	H | qureg[9]
	Rx(theta[2]) | qureg[8]
	H | qureg[2]
	Rx(theta[0]) | qureg[3]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[3]
	H | qureg[2]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[11]
	H | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[13]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[1]
	H | qureg[2]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[3]
	H | qureg[2]
	H | qureg[1]
	H | qureg[4]
	H | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[12]
	H | qureg[11]
	H | qureg[4]
	H | qureg[1]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[5]
	H | qureg[11]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[13]
	H | qureg[11]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[1]
	Rx(theta[0]) | qureg[6]
	H | qureg[7]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[6], qureg[7] )
	H | qureg[13]
	H | qureg[12]
	H | qureg[7]
	Rx(theta[2]) | qureg[6]
	H | qureg[1]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[5]
	H | qureg[1]
	Rx(theta[0]) | qureg[2]
	H | qureg[3]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[11]
	H | qureg[10]
	H | qureg[3]
	Rx(theta[2]) | qureg[2]
	Rx(theta[0]) | qureg[8]
	H | qureg[9]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[8], qureg[9] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[9]
	Rx(theta[2]) | qureg[8]
	H | qureg[0]
	H | qureg[1]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	H | qureg[1]
	H | qureg[0]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[4]
	H | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[13]
	H | qureg[10]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[1]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[5]
	H | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[12]
	H | qureg[11]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[2]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[1]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[1]
	Rx(theta[2]) | qureg[0]
	H | qureg[2]
	H | qureg[5]
	H | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[12]
	H | qureg[11]
	H | qureg[5]
	H | qureg[2]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[10]
	H | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[12]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[2]
	H | qureg[1]
	H | qureg[5]
	H | qureg[11]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[13]
	H | qureg[11]
	H | qureg[5]
	H | qureg[1]
	Rx(theta[0]) | qureg[1]
	H | qureg[4]
	H | qureg[10]
	H | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[13]
	H | qureg[10]
	H | qureg[4]
	Rx(theta[2]) | qureg[1]
	Rx(theta[0]) | qureg[0]
	H | qureg[1]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[1]
	Rx(theta[2]) | qureg[0]
	Rx(theta[0]) | qureg[0]
	H | qureg[4]
	H | qureg[10]
	H | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[12]
	H | qureg[10]
	H | qureg[4]
	Rx(theta[2]) | qureg[0]
	H | qureg[8]
	Rx(theta[0]) | qureg[9]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[8], qureg[9] )
	H | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[9]
	H | qureg[8]
	H | qureg[4]
	H | qureg[5]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[0]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[4], qureg[5] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	H | qureg[5]
	H | qureg[4]
	H | qureg[2]
	H | qureg[3]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[3]
	H | qureg[2]
	H | qureg[6]
	Rx(theta[0]) | qureg[7]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[6], qureg[7] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[7]
	H | qureg[6]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[0]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[3]
	Rx(theta[2]) | qureg[2]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[11]
	H | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[13]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[3]
	Rx(theta[0]) | qureg[0]
	H | qureg[1]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[13]
	H | qureg[12]
	H | qureg[1]
	Rx(theta[2]) | qureg[0]
	H | qureg[2]
	H | qureg[3]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[1]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	H | qureg[3]
	H | qureg[2]
	H | qureg[3]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[5]
	H | qureg[3]
	H | qureg[1]
	H | qureg[4]
	H | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[13]
	H | qureg[10]
	H | qureg[4]
	H | qureg[1]
	H | qureg[2]
	H | qureg[5]
	H | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[13]
	H | qureg[10]
	H | qureg[5]
	H | qureg[2]
	Rx(theta[0]) | qureg[2]
	H | qureg[5]
	H | qureg[11]
	H | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[12]
	H | qureg[11]
	H | qureg[5]
	Rx(theta[2]) | qureg[2]
	Rx(theta[0]) | qureg[2]
	H | qureg[3]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[0]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[13]
	H | qureg[12]
	H | qureg[3]
	Rx(theta[2]) | qureg[2]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[10]
	H | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[13]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[0]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[5]
	H | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[13]
	H | qureg[10]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[2]
	H | qureg[4]
	Rx(theta[0]) | qureg[5]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	H | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[5]
	H | qureg[4]
	H | qureg[3]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[4]
	H | qureg[3]
	H | qureg[8]
	H | qureg[9]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[8], qureg[9] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[9]
	H | qureg[8]
	Rx(theta[0]) | qureg[0]
	H | qureg[1]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[1]
	Rx(theta[2]) | qureg[0]
	H | qureg[3]
	Rx(theta[0]) | qureg[5]
	H | qureg[11]
	H | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[13]
	H | qureg[11]
	Rx(theta[2]) | qureg[5]
	H | qureg[3]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[11]
	H | qureg[12]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[12]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[3]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[1]
	Rx(theta[2]) | qureg[0]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[4], qureg[5] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[4]
	H | qureg[3]
	H | qureg[4]
	Rx(theta[0]) | qureg[10]
	H | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[13]
	Rx(theta[2]) | qureg[10]
	H | qureg[4]
	H | qureg[3]
	H | qureg[2]
	H | qureg[4]
	Rx(theta[0]) | qureg[10]
	H | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[12]
	Rx(theta[2]) | qureg[10]
	H | qureg[4]
	H | qureg[2]
	Rx(theta[0]) | qureg[1]
	H | qureg[4]
	H | qureg[11]
	H | qureg[12]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[12]
	H | qureg[11]
	H | qureg[4]
	Rx(theta[2]) | qureg[1]
	H | qureg[3]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[11]
	H | qureg[3]
	H | qureg[4]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	Rx(theta[2]) | qureg[12]
	H | qureg[4]
	H | qureg[4]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[0]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[4], qureg[5] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[5]
	H | qureg[4]
	Rx(theta[0]) | qureg[6]
	Rx(theta[0]) | qureg[7]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[0]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[6], qureg[7] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[7]
	Rx(theta[2]) | qureg[6]
	H | qureg[2]
	H | qureg[4]
	H | qureg[10]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[12]
	H | qureg[10]
	H | qureg[4]
	H | qureg[2]
	H | qureg[0]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[1]
	H | qureg[0]
	Rx(theta[0]) | qureg[6]
	H | qureg[7]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[6], qureg[7] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[7]
	Rx(theta[2]) | qureg[6]
	Rx(theta[0]) | qureg[0]
	H | qureg[5]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[11]
	H | qureg[5]
	Rx(theta[2]) | qureg[0]
	H | qureg[8]
	Rx(theta[0]) | qureg[9]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[0]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	H | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[9]
	H | qureg[8]
	Rx(theta[0]) | qureg[6]
	H | qureg[7]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[6], qureg[7] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[7]
	Rx(theta[2]) | qureg[6]
	H | qureg[0]
	Rx(theta[0]) | qureg[10]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	Rz(theta[1]) | qureg[10]
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[10]
	H | qureg[0]
	H | qureg[0]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[1]
	H | qureg[0]
	H | qureg[3]
	H | qureg[5]
	H | qureg[11]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[13]
	H | qureg[11]
	H | qureg[5]
	H | qureg[3]
	Rx(theta[0]) | qureg[2]
	H | qureg[4]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[10]
	H | qureg[4]
	Rx(theta[2]) | qureg[2]
	H | qureg[8]
	Rx(theta[0]) | qureg[9]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[8], qureg[9] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[9]
	H | qureg[8]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[11]
	H | qureg[12]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[12]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[1]
	H | qureg[3]
	H | qureg[5]
	Rx(theta[0]) | qureg[11]
	H | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[13]
	Rx(theta[2]) | qureg[11]
	H | qureg[5]
	H | qureg[3]
	Rx(theta[0]) | qureg[6]
	Rx(theta[0]) | qureg[7]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[6], qureg[7] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[7]
	Rx(theta[2]) | qureg[6]
	Rx(theta[0]) | qureg[1]
	H | qureg[4]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[11]
	H | qureg[4]
	Rx(theta[2]) | qureg[1]
	Rx(theta[0]) | qureg[4]
	H | qureg[5]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[4], qureg[5] )
	H | qureg[13]
	H | qureg[12]
	H | qureg[5]
	Rx(theta[2]) | qureg[4]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[5]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[4]
	H | qureg[0]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[3]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[4]
	H | qureg[0]
	Rx(theta[0]) | qureg[4]
	H | qureg[5]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[0]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[4], qureg[5] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[5]
	Rx(theta[2]) | qureg[4]
	Rx(theta[0]) | qureg[3]
	H | qureg[4]
	H | qureg[10]
	H | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[13]
	H | qureg[10]
	H | qureg[4]
	Rx(theta[2]) | qureg[3]
	H | qureg[2]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[4]
	H | qureg[2]
	H | qureg[0]
	H | qureg[4]
	Rx(theta[0]) | qureg[10]
	H | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[3]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[12]
	Rx(theta[2]) | qureg[10]
	H | qureg[4]
	H | qureg[0]
	H | qureg[2]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[5]
	H | qureg[2]
	H | qureg[6]
	Rx(theta[0]) | qureg[7]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[0]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[6], qureg[7] )
	H | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[7]
	H | qureg[6]
	Rx(theta[0]) | qureg[0]
	H | qureg[4]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[3]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[10]
	H | qureg[4]
	Rx(theta[2]) | qureg[0]
	Rx(theta[0]) | qureg[1]
	H | qureg[4]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[10]
	H | qureg[4]
	Rx(theta[2]) | qureg[1]
	H | qureg[3]
	H | qureg[4]
	H | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[13]
	H | qureg[10]
	H | qureg[4]
	H | qureg[3]
	Rx(theta[0]) | qureg[6]
	Rx(theta[0]) | qureg[7]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[0]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[6], qureg[7] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[7]
	Rx(theta[2]) | qureg[6]
	Rx(theta[0]) | qureg[1]
	H | qureg[5]
	H | qureg[11]
	H | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[13]
	H | qureg[11]
	H | qureg[5]
	Rx(theta[2]) | qureg[1]
	Rx(theta[0]) | qureg[3]
	H | qureg[5]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[11]
	H | qureg[5]
	Rx(theta[2]) | qureg[3]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[3]
	Rx(theta[2]) | qureg[2]
	Rx(theta[0]) | qureg[0]
	H | qureg[1]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[1]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[11]
	H | qureg[10]
	H | qureg[1]
	Rx(theta[2]) | qureg[0]
	Rx(theta[0]) | qureg[0]
	H | qureg[5]
	H | qureg[11]
	H | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[12]
	H | qureg[11]
	H | qureg[5]
	Rx(theta[2]) | qureg[0]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[1]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[1]
	Rx(theta[2]) | qureg[0]
	H | qureg[5]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	Rx(theta[2]) | qureg[13]
	H | qureg[5]
	H | qureg[2]
	Rx(theta[0]) | qureg[3]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[0]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[3]
	H | qureg[2]
	Rx(theta[0]) | qureg[6]
	H | qureg[7]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[0]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[6], qureg[7] )
	H | qureg[11]
	H | qureg[10]
	H | qureg[7]
	Rx(theta[2]) | qureg[6]
	Rx(theta[0]) | qureg[4]
	H | qureg[12]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	H | qureg[12]
	Rx(theta[2]) | qureg[4]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[4]
	H | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[12]
	H | qureg[11]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[1]
	Rx(theta[0]) | qureg[3]
	H | qureg[5]
	H | qureg[11]
	H | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[13]
	H | qureg[11]
	H | qureg[5]
	Rx(theta[2]) | qureg[3]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[4]
	H | qureg[10]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[12]
	H | qureg[10]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[0]
	H | qureg[2]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[5]
	H | qureg[2]
	Rx(theta[0]) | qureg[2]
	H | qureg[10]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	Rz(theta[3]) | qureg[10]
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[10]
	Rx(theta[2]) | qureg[2]
	Rx(theta[0]) | qureg[1]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[10]
	H | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[13]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[1]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[10]
	H | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[13]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[3]
	H | qureg[2]
	Rx(theta[0]) | qureg[5]
	H | qureg[11]
	H | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[12]
	H | qureg[11]
	Rx(theta[2]) | qureg[5]
	H | qureg[2]
	Rx(theta[0]) | qureg[8]
	H | qureg[9]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[9]
	Rx(theta[2]) | qureg[8]
	H | qureg[2]
	H | qureg[5]
	Rx(theta[0]) | qureg[11]
	H | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[12]
	Rx(theta[2]) | qureg[11]
	H | qureg[5]
	H | qureg[2]
	H | qureg[8]
	Rx(theta[0]) | qureg[9]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[9]
	H | qureg[8]
	Rx(theta[0]) | qureg[3]
	H | qureg[11]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[3]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[11]
	Rx(theta[2]) | qureg[3]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[4]
	H | qureg[10]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[12]
	H | qureg[10]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[2]
	H | qureg[4]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[5]
	H | qureg[4]
	Rx(theta[0]) | qureg[2]
	H | qureg[5]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[10]
	H | qureg[5]
	Rx(theta[2]) | qureg[2]
	H | qureg[2]
	Rx(theta[0]) | qureg[10]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	Rz(theta[2]) | qureg[10]
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[10]
	H | qureg[2]
	Rx(theta[0]) | qureg[4]
	H | qureg[5]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[5]
	Rx(theta[2]) | qureg[4]
	H | qureg[2]
	Rx(theta[0]) | qureg[5]
	H | qureg[10]
	H | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[13]
	H | qureg[10]
	Rx(theta[2]) | qureg[5]
	H | qureg[2]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[10]
	H | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[12]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[0]
	H | qureg[0]
	H | qureg[5]
	Rx(theta[0]) | qureg[10]
	H | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[13]
	Rx(theta[2]) | qureg[10]
	H | qureg[5]
	H | qureg[0]
	H | qureg[3]
	H | qureg[4]
	H | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[12]
	H | qureg[11]
	H | qureg[4]
	H | qureg[3]
	H | qureg[0]
	H | qureg[5]
	H | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[12]
	H | qureg[11]
	H | qureg[5]
	H | qureg[0]
	Rx(theta[0]) | qureg[2]
	H | qureg[5]
	H | qureg[10]
	H | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[13]
	H | qureg[10]
	H | qureg[5]
	Rx(theta[2]) | qureg[2]
	H | qureg[6]
	Rx(theta[0]) | qureg[7]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[6], qureg[7] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[7]
	H | qureg[6]
	Rx(theta[0]) | qureg[8]
	Rx(theta[0]) | qureg[9]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[8], qureg[9] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[9]
	Rx(theta[2]) | qureg[8]
	Rx(theta[0]) | qureg[0]
	H | qureg[5]
	H | qureg[10]
	H | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[13]
	H | qureg[10]
	H | qureg[5]
	Rx(theta[2]) | qureg[0]
	Rx(theta[0]) | qureg[3]
	H | qureg[4]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[11]
	H | qureg[4]
	Rx(theta[2]) | qureg[3]
	H | qureg[4]
	H | qureg[5]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[5]
	H | qureg[4]
	H | qureg[1]
	H | qureg[4]
	Rx(theta[0]) | qureg[11]
	H | qureg[12]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[12]
	Rx(theta[2]) | qureg[11]
	H | qureg[4]
	H | qureg[1]
	H | qureg[4]
	Rx(theta[0]) | qureg[5]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[4], qureg[5] )
	H | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[5]
	H | qureg[4]
	H | qureg[0]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[5]
	H | qureg[0]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[11]
	H | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[12]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[0]
	H | qureg[1]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[4]
	H | qureg[1]
	H | qureg[2]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[1]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[3]
	H | qureg[2]
	Rx(theta[0]) | qureg[2]
	H | qureg[3]
	Rx(theta[0]) | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[3]
	Rx(theta[2]) | qureg[2]
	Rx(theta[0]) | qureg[1]
	H | qureg[11]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[0]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[11]
	Rx(theta[2]) | qureg[1]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[5]
	H | qureg[11]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[13]
	H | qureg[11]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[3]
	H | qureg[4]
	H | qureg[5]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	H | qureg[5]
	H | qureg[4]
	Rx(theta[0]) | qureg[4]
	H | qureg[5]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	H | qureg[11]
	H | qureg[10]
	H | qureg[5]
	Rx(theta[2]) | qureg[4]
	H | qureg[0]
	Rx(theta[0]) | qureg[4]
	H | qureg[10]
	H | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[12]
	H | qureg[10]
	Rx(theta[2]) | qureg[4]
	H | qureg[0]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[11]
	H | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[12]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[2]
	H | qureg[6]
	H | qureg[7]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[6], qureg[7] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	H | qureg[7]
	H | qureg[6]
	H | qureg[6]
	H | qureg[7]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[6], qureg[7] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[7]
	H | qureg[6]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[5]
	H | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[13]
	H | qureg[10]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[0]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[5]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[4], qureg[5] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[4]
	H | qureg[3]
	Rx(theta[0]) | qureg[4]
	H | qureg[11]
	H | qureg[12]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[12]
	H | qureg[11]
	Rx(theta[2]) | qureg[4]
	H | qureg[3]
	H | qureg[6]
	Rx(theta[0]) | qureg[7]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[6], qureg[7] )
	H | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[7]
	H | qureg[6]
	H | qureg[0]
	H | qureg[1]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[1]
	H | qureg[0]
	H | qureg[2]
	H | qureg[3]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	H | qureg[3]
	H | qureg[2]
	H | qureg[1]
	Rx(theta[0]) | qureg[4]
	H | qureg[10]
	H | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[13]
	H | qureg[10]
	Rx(theta[2]) | qureg[4]
	H | qureg[1]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[5]
	H | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[12]
	H | qureg[11]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[0]
	H | qureg[0]
	Rx(theta[0]) | qureg[1]
	H | qureg[12]
	H | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[1], qureg[12] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[1]
	H | qureg[0]
	H | qureg[0]
	H | qureg[5]
	Rx(theta[0]) | qureg[11]
	H | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[12]
	Rx(theta[2]) | qureg[11]
	H | qureg[5]
	H | qureg[0]
	H | qureg[4]
	H | qureg[5]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[0]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[5], qureg[12] )
	CX | ( qureg[4], qureg[5] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	H | qureg[5]
	H | qureg[4]
	Rx(theta[0]) | qureg[1]
	H | qureg[5]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[11]
	H | qureg[5]
	Rx(theta[2]) | qureg[1]
	H | qureg[3]
	H | qureg[4]
	Rx(theta[0]) | qureg[11]
	H | qureg[12]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[12]
	Rx(theta[2]) | qureg[11]
	H | qureg[4]
	H | qureg[3]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[3]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[3]
	Rx(theta[2]) | qureg[2]
	H | qureg[1]
	Rx(theta[0]) | qureg[4]
	H | qureg[11]
	H | qureg[12]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[12]
	H | qureg[11]
	Rx(theta[2]) | qureg[4]
	H | qureg[1]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[3]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[0]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[3], qureg[12] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[3]
	Rx(theta[2]) | qureg[2]
	Rx(theta[0]) | qureg[6]
	Rx(theta[0]) | qureg[7]
	Rx(theta[0]) | qureg[12]
	H | qureg[13]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[7], qureg[12] )
	CX | ( qureg[6], qureg[7] )
	H | qureg[13]
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[7]
	Rx(theta[2]) | qureg[6]
	H | qureg[0]
	Rx(theta[0]) | qureg[5]
	H | qureg[10]
	H | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[2]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[13]
	H | qureg[10]
	Rx(theta[2]) | qureg[5]
	H | qureg[0]
	H | qureg[3]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[4]
	H | qureg[3]
	H | qureg[0]
	Rx(theta[0]) | qureg[5]
	H | qureg[11]
	H | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[12]
	H | qureg[11]
	Rx(theta[2]) | qureg[5]
	H | qureg[0]
	H | qureg[8]
	H | qureg[9]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	H | qureg[9]
	H | qureg[8]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[4]
	H | qureg[0]
	H | qureg[1]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[4]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[1]
	H | qureg[0]
	H | qureg[1]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[1]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[11]
	H | qureg[1]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[4]
	H | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[12]
	H | qureg[11]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[3]
	H | qureg[1]
	Rx(theta[0]) | qureg[5]
	H | qureg[11]
	H | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[13]
	H | qureg[11]
	Rx(theta[2]) | qureg[5]
	H | qureg[1]
	H | qureg[8]
	H | qureg[9]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[8], qureg[9] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	H | qureg[9]
	H | qureg[8]
	Rx(theta[0]) | qureg[3]
	Rx(theta[0]) | qureg[4]
	H | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	Rx(theta[2]) | qureg[13]
	H | qureg[10]
	Rx(theta[2]) | qureg[4]
	Rx(theta[2]) | qureg[3]
	Rx(theta[0]) | qureg[8]
	Rx(theta[0]) | qureg[9]
	H | qureg[12]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[9], qureg[12] )
	CX | ( qureg[8], qureg[9] )
	Rx(theta[2]) | qureg[13]
	H | qureg[12]
	Rx(theta[2]) | qureg[9]
	Rx(theta[2]) | qureg[8]
	Rx(theta[0]) | qureg[0]
	Rx(theta[0]) | qureg[1]
	H | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[1]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[1]
	Rx(theta[2]) | qureg[0]
	Rx(theta[0]) | qureg[2]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[10]
	H | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[13]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[5]
	Rx(theta[2]) | qureg[2]
	H | qureg[2]
	Rx(theta[0]) | qureg[4]
	H | qureg[10]
	H | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[12]
	H | qureg[10]
	Rx(theta[2]) | qureg[4]
	H | qureg[2]
	Rx(theta[0]) | qureg[5]
	H | qureg[13]
	CX | ( qureg[5], qureg[6] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[7], qureg[8] )
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[5], qureg[6] )
	H | qureg[13]
	Rx(theta[2]) | qureg[5]
	Rx(theta[0]) | qureg[8]
	Rx(theta[0]) | qureg[9]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[0]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[9]
	Rx(theta[2]) | qureg[8]
	H | qureg[0]
	H | qureg[4]
	H | qureg[10]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[3]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[12]
	H | qureg[10]
	H | qureg[4]
	H | qureg[0]
	H | qureg[0]
	H | qureg[5]
	H | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[13]
	H | qureg[10]
	H | qureg[5]
	H | qureg[0]
	Rx(theta[0]) | qureg[3]
	H | qureg[4]
	H | qureg[11]
	H | qureg[12]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[4]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[4], qureg[11] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[12]
	H | qureg[11]
	H | qureg[4]
	Rx(theta[2]) | qureg[3]
	H | qureg[3]
	Rx(theta[0]) | qureg[4]
	H | qureg[10]
	H | qureg[13]
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	H | qureg[13]
	H | qureg[10]
	Rx(theta[2]) | qureg[4]
	H | qureg[3]
	H | qureg[1]
	H | qureg[4]
	Rx(theta[0]) | qureg[10]
	H | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[13]
	Rx(theta[2]) | qureg[10]
	H | qureg[4]
	H | qureg[1]
	H | qureg[1]
	H | qureg[5]
	Rx(theta[0]) | qureg[11]
	H | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[3]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	H | qureg[13]
	Rx(theta[2]) | qureg[11]
	H | qureg[5]
	H | qureg[1]
	H | qureg[0]
	Rx(theta[0]) | qureg[5]
	Rx(theta[0]) | qureg[11]
	Rx(theta[0]) | qureg[12]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[1]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[5], qureg[11] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[0], qureg[1] )
	Rx(theta[2]) | qureg[12]
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[5]
	H | qureg[0]
	Rx(theta[0]) | qureg[2]
	H | qureg[4]
	H | qureg[10]
	H | qureg[12]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	Rz(theta[2]) | qureg[12]
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[12]
	H | qureg[10]
	H | qureg[4]
	Rx(theta[2]) | qureg[2]
	H | qureg[2]
	H | qureg[5]
	Rx(theta[0]) | qureg[10]
	H | qureg[13]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[4]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[5], qureg[10] )
	CX | ( qureg[4], qureg[5] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	H | qureg[13]
	Rx(theta[2]) | qureg[10]
	H | qureg[5]
	H | qureg[2]
	Rx(theta[0]) | qureg[8]
	H | qureg[9]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[8], qureg[9] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[0]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[9], qureg[10] )
	CX | ( qureg[8], qureg[9] )
	H | qureg[11]
	H | qureg[10]
	H | qureg[9]
	Rx(theta[2]) | qureg[8]
	Rx(theta[0]) | qureg[2]
	H | qureg[3]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[11]
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[1]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[3], qureg[10] )
	CX | ( qureg[2], qureg[3] )
	Rx(theta[2]) | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[3]
	Rx(theta[2]) | qureg[2]
	H | qureg[6]
	H | qureg[7]
	Rx(theta[0]) | qureg[10]
	H | qureg[11]
	CX | ( qureg[6], qureg[7] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[2]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[7], qureg[10] )
	CX | ( qureg[6], qureg[7] )
	H | qureg[11]
	Rx(theta[2]) | qureg[10]
	H | qureg[7]
	H | qureg[6]
	H | qureg[0]
	Rx(theta[0]) | qureg[1]
	H | qureg[10]
	H | qureg[11]
	CX | ( qureg[0], qureg[1] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	Rz(theta[1]) | qureg[11]
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[1], qureg[10] )
	CX | ( qureg[0], qureg[1] )
	H | qureg[11]
	H | qureg[10]
	Rx(theta[2]) | qureg[1]
	H | qureg[0]
	H | qureg[1]
	Rx(theta[0]) | qureg[4]
	Rx(theta[0]) | qureg[10]
	Rx(theta[0]) | qureg[13]
	CX | ( qureg[1], qureg[2] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[12], qureg[13] )
	Rz(theta[1]) | qureg[13]
	CX | ( qureg[12], qureg[13] )
	CX | ( qureg[11], qureg[12] )
	CX | ( qureg[10], qureg[11] )
	CX | ( qureg[4], qureg[10] )
	CX | ( qureg[3], qureg[4] )
	CX | ( qureg[2], qureg[3] )
	CX | ( qureg[1], qureg[2] )
	Rx(theta[2]) | qureg[13]
	Rx(theta[2]) | qureg[10]
	Rx(theta[2]) | qureg[4]
	H | qureg[1]
# Function that need to be implemented by the contestants
def calculate_theta(eng, final_state):
	"""
	Calculate the optimal theta value.
	Args:
		eng (MainEngine): Main compiler engine to use.
		final_state (list): list of quantum bit states.
	Returns:
		list of best theta values.
	"""
	return [0, 0, 0, 0, 0]
if __name__ == "__main__":
	# use projectq simulator
	#eng = MainEngine()
	# use hiq simulator
	backend = SimulatorMPI(gate_fusion=True)
	cache_depth = 10
	rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
	engines = [TagRemover()
		, LocalOptimizer(cache_depth)
		, AutoReplacer(rule_set)
		, TagRemover()
		, LocalOptimizer(cache_depth)
		, GreedyScheduler()
		]
	# make the compiler and run the circuit on the simulator backend
	eng = HiQMainEngine(backend, engines)
	qureg = eng.allocate_qureg(14)
	final_state = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
	# Function that need to be implemented by the contestants
	theta = calculate_theta(eng, final_state)
	run_circuit(qureg, theta)
	eng.flush()
	print(eng.backend.get_probability(final_state, qureg))
	All(Measure) | qureg