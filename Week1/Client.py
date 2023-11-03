from __future__ import print_function

import logging

import grpc
import QuadraticEquation_pb2
import QuadraticEquation_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = QuadraticEquation_pb2_grpc.QuadraticEquationStub(channel)
        response = stub.quadraticEquation(str)

        a = input("Enter coefficient a: ")
        b = input("Enter coefficient b: ")
        c = input("Enter coefficient c: ")

        coefficients = QuadraticEquation_pb2.Coefficients(a=a, b=b, c=c)
        response = stub.quadraticEquation(coefficients)

        print(response.x1)
        print(response.x2)

if __name__ == "__main__":
    logging.basicConfig()
    run()
