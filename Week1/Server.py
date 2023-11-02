from concurrent import futures
import logging

import grpc
import QuadraticEquation_pb2
import QuadraticEquation_pb2_grpc

import QuadraticEquation


class QuadraticEquationServicer(QuadraticEquation_pb2_grpc.QuadraticEquationServicer):

    def quadraticEquation(self, request, context):
        response = QuadraticEquation_pb2.Coefficients()
        response.value = QuadraticEquation.quadraticEquation(request.value)
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
