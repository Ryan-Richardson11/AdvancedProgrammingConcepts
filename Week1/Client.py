from __future__ import print_function

import logging

import grpc
import QuadraticEquation_pb2
import QuadraticEquation_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = QuadraticEquation_pb2_grpc.QuadraticEquationStub(channel)
        response = stub.quadraticEquation(str)

        print(response.value)


if __name__ == "__main__":
    logging.basicConfig()
    run()
