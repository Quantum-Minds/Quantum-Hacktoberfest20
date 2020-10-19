# Program to generate a 16 bit random number on a quantum computer.
# Contributed by Shubh Bansal(http://github.com/proRamLOGO).
#IBM Qiskit Framework USED

#Imports
from qiskit import *
from qiskit.tools.visualization import plot_histogram

#Accuire 16 Qubits and 16 CBits
qr = QuantumRegister(16)
cr = ClassicalRegister(16)
circuit = QuantumCircuit(qr,cr)

%matplotlib inline

# Put all the qubits into superposition
for i in range(16) :
    circuit.h(qr[i])

# Measure all the qubits
circuit.measure(qr,cr)
circuit.draw(output='mpl')

# Run the shots
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit,backend=simulator).result()
plot_histogram(result.get_counts(circuit))

# Multiple numbers would have been generated we can select any of them.
# Here the number chosen had maximum frequency among all the shots.
res = result.get_counts(circuit)
randomBinary = max(res,key=res.get)
randomInt = int(randomBinary,2)

print(randomInt)
