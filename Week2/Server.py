from concurrent import futures
import logging

import grpc
import QuadraticEquation_pb2
import QuadraticEquation_pb2_grpc

from QuadraticEquation import quadraticEquation


class QuadraticEquationServicer(QuadraticEquation_pb2_grpc.QuadraticEquationServicer):

    def quadraticEquation(self, request, context):
        # Takes in 3 requested values as parameters
        a = request.a
        b = request.b
        c = request.c

        # Returns response as solution identified in .proto file
        response = QuadraticEquation_pb2.Solution()

        # Checks functions result then sends back response to client
        result = quadraticEquation(a, b, c)
        if result == None:
            response.x1 = "The answer does not exist."
            response.x2 = "The answer does not exist."
        else:
            response.x1 = result[0]
            response.x2 = result[1]
        return response

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    QuadraticEquation_pb2_grpc.add_QuadraticEquationServicer_to_server(
        QuadraticEquationServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
