import grpc
from concurrent import futures
import time

import saludo_pb2
import saludo_pb2_grpc

# Implementación del servicio
class SaludoServiceServicer(saludo_pb2_grpc.SaludoServiceServicer):
    def ObtenerSaludo(self, request, context):
        print(f"Recibida solicitud de saludo para: {request.nombre}")
        mensaje_respuesta = f"¡Hola, {request.nombre}! Saludos desde gRPC."
        return saludo_pb2.SaludoResponse(mensaje=mensaje_respuesta)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    saludo_pb2_grpc.add_SaludoServiceServicer_to_server(
        SaludoServiceServicer(), server)
    server.add_insecure_port('[::]:50051') # Escucha en el puerto 50051
    server.start()
    print("Servidor gRPC iniciado en el puerto 50051...")
    try:
        while True:
            time.sleep(86400) # Mantener el servidor corriendo por un día
    except KeyboardInterrupt:
        server.stop(0)
        print("Servidor gRPC detenido.")

if __name__ == '__main__':
    serve()