# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import QuadraticEquation_pb2 as QuadraticEquation__pb2


class QuadraticEquationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.quadraticEquation = channel.unary_unary(
            '/QuadraticEquation/quadraticEquation',
            request_serializer=QuadraticEquation__pb2.Coefficients.SerializeToString,
            response_deserializer=QuadraticEquation__pb2.Solution.FromString,
        )


class QuadraticEquationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def quadraticEquation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QuadraticEquationServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'quadraticEquation': grpc.unary_unary_rpc_method_handler(
            servicer.quadraticEquation,
            request_deserializer=QuadraticEquation__pb2.Coefficients.FromString,
            response_serializer=QuadraticEquation__pb2.Solution.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'QuadraticEquation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class QuadraticEquation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def quadraticEquation(request,
                          target,
                          options=(),
                          channel_credentials=None,
                          call_credentials=None,
                          insecure=False,
                          compression=None,
                          wait_for_ready=None,
                          timeout=None,
                          metadata=None):
        return grpc.experimental.unary_unary(request, target, '/QuadraticEquation/quadraticEquation',
                                             QuadraticEquation__pb2.Coefficients.SerializeToString,
                                             QuadraticEquation__pb2.Solution.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
