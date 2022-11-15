from database import voting_db

def compute_vote(block):
    voting_db.insert(block)

def get_chain():
    return voting_db.fetch().items

def get_first_block():
    return voting_db.fetch({"index":1}).items[0]