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

    def mine(self, target):
        return True


blockchain = Blockchain()
proof = blockchain.proofOfWork(1)
print(proof)
