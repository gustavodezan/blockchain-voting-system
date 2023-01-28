from fastapi import FastAPI
from blockchain import Blockchain
import crud

def load_chain(blockchain):
    blockchain.chain = []
    chain = sorted(crud.get_chain(), key=lambda k: k['index'])
    for block in chain:
        block.pop("key")
        blockchain.chain.append(block)

app = FastAPI()

blockchain = Blockchain()
if len(crud.get_chain()) <= 0:
    crud.compute_vote(blockchain.chain[0])
else:
    load_chain(blockchain)

@app.post('/vote/{vote_id}')
def mine_block(vote_id: str):
    """Register a new vote into the system and create a new block on the chain"""
    load_chain(blockchain)
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash, vote_id)

    response = {
        'message': 'Block mined',
        'index': block['index'],
        'candidate_id': block['candidate_id'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
        }
    
    crud.compute_vote(block)
    
    return response

@app.get('/chain')
def display_chain():
    """Returns the chain"""
    load_chain(blockchain)
    return {'chain': blockchain.chain, 'length': len(blockchain.chain)}

# check validity
@app.get('/validate')
def validate():
    """Check if the structure of the chain is valid"""
    load_chain(blockchain)
    
    valid = blockchain.chain_valid(blockchain.chain)
    
    if valid:
        return {'message': 'The blockchain is valid'}
    else:
        return {'message': 'Blockchain invalid!'}

@app.get('/result')
def get_result():
    """Return the number of votes per candidate"""
    load_chain(blockchain)
    votes = blockchain.chain[1:]
    result = {}
    for vote in votes:
        if vote['candidate_id'] in result:
            result[vote['candidate_id']] += 1
        else:
            result[vote['candidate_id']] = 1
    return result