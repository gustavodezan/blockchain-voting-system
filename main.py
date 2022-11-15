from fastapi import FastAPI
from blockchain import Blockchain
import crud

app = FastAPI()

blockchain = Blockchain()
if len(crud.get_chain()) <= 0:
    crud.compute_vote(blockchain.chain[0])
    pass
else:
    blockchain.chain = []
    chain = sorted(crud.get_chain(), key=lambda k: k['index'])
    for block in chain:
        block.pop("key")
        blockchain.chain.append(block)


@app.get('/mine_block/{vote_id}')
def mine_block(vote_id: str):
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash, vote_id)

    response = {
        'message': 'Block mined',
        'index': block['index'],
        'transaction_id': block['transaction_id'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
        }
    
    crud.compute_vote(block)
    
    return response

@app.get('/chain')
def display_chain():
    chain = crud.get_chain()
    return {'chain': blockchain.chain, 'length': len(blockchain.chain)}

# check validity
@app.get('/validate')
def validate():
    # blockchain.chain = []
    # for block in chain_list:
    #     blockchain.chain.append(block)
    
    # blockchain.chain = sorted(blockchain.chain, key=lambda k: k['index'])
    valid = blockchain.chain_valid(blockchain.chain)
    
    if valid:
        return {'message': 'The blockchain is valid'}
    else:
        return {'message': 'Blockchain invalid!'}