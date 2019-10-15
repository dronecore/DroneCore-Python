# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import shell_pb2 as shell__pb2


class ShellServiceStub(object):
  """*
  Shell Service allow to communicate with vehicle's system shell.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SetShellMessage = channel.unary_unary(
        '/mavsdk.rpc.shell.ShellService/SetShellMessage',
        request_serializer=shell__pb2.SetShellMessageRequest.SerializeToString,
        response_deserializer=shell__pb2.SetShellMessageResponse.FromString,
        )


class ShellServiceServicer(object):
  """*
  Shell Service allow to communicate with vehicle's system shell.
  """

  def SetShellMessage(self, request, context):
    """Communicate with a vehicle's Shell.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ShellServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SetShellMessage': grpc.unary_unary_rpc_method_handler(
          servicer.SetShellMessage,
          request_deserializer=shell__pb2.SetShellMessageRequest.FromString,
          response_serializer=shell__pb2.SetShellMessageResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mavsdk.rpc.shell.ShellService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))