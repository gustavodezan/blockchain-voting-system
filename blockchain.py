# Python blockchain
from datetime import datetime
import hashlib
import json

class Blockchain:
    # when the blockchain is instatiated it's create the very first block with hash 0
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0', transaction_id=None)
    
    def create_block(self, proof: int, previous_hash: str, transaction_id: str):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'candidate_id': transaction_id,
            'proof': proof,
            'previous_hash':previous_hash
        }
        self.chain.append(block)
        return block
    
    def print_previous_block(self):
        return self.chain[-1]
    
    # mine
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof).encode()).hexdigest()
            
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof

    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            #print(self.hash(previous_block))
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            previous_block = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_block).encode()).hexdigest()
            
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1

        return True
