import grpc

import saludo_pb2
import saludo_pb2_grpc

def run():
    # Conectarse al servidor gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = saludo_pb2_grpc.SaludoServiceStub(channel)

        # Crear una solicitud de saludo
        nombre_usuario = input("Ingresa tu nombre para el saludo: ")
        request = saludo_pb2.SaludoRequest(nombre=nombre_usuario)

        try:
            # Llamar al método ObtenerSaludo del servicio
            response = stub.ObtenerSaludo(request)
            print(f"Respuesta del servidor: {response.mensaje}")
        except grpc.RpcError as e:
            print(f"Error al llamar al servicio: {e.details()}")

if __name__ == '__main__':
    run()