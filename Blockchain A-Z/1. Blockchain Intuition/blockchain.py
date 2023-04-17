# Module 1 - Create a Blockchain

import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:

    def __init__(self):
        self.chain = []
        self.createBlock(proof=1, previousHash='0')
        print("hi")

    def createBlock(self, proof, previousHash, data={}):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'data': {},
            'previousHash': previousHash,
        }
        self.chain.append(block)
        return block

    def getPreviousBlock(self):
        return self.chain[-1]

    def proofOfWork(self, previousProof):
        newProof = 1
        validProof = False
        while validProof is False:
            hashOperation = hashlib.sha256(
                str(newProof**2 - previousProof**2).encode()).hexdigest()
            if hashOperation[0:4] == '0000':
                validProof = True
            newProof += 1
        return newProof

    def hash(self, block):
        encodedBlock = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()

    def isBlockchainValid(self, chain):
        blockIndex = 1
        previousBlock = chain[0]
        while blockIndex < len(chain):
            block = chain[blockIndex]
            if block['previousHash'] != self.hash(previousBlock):
                return False
            previousProof = self.proofOfWork(previousBlock['proof'])
            # here we check if the current proof generates a valid PoW
            proof = block['proof']
            hashOperation = hashlib.sha256(
                str(proof**2 - previousProof**2).encode()).hexdigest()
            if hashOperation[0:4] != '0000':
                return False
            previousBlock = chain[blockIndex]
            blockIndex += 1
        return True

    def mine(self, target):
        return True


blockchain = Blockchain()
proof = blockchain.proofOfWork(1)
print(proof)
