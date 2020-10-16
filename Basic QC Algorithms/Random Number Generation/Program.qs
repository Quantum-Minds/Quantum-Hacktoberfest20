namespace QuantumRandomNumberGeneration {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    @EntryPoint()
    operation GenerateRandomBit() : Result {
      
        using (q = Qubit()) {
           
            H(q);
    
            return MResetZ(q);
        }
    }
}
