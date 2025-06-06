# from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# app = FastAPI()


# @app.websocket("/messaging")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     try:
#         while True:
#             data = await websocket.receive_text()
#             print(f"Received data {data}")
#             await websocket.send_text(data)
#     except WebSocketDisconnect:
#         print(f"client disconnected")


# # 포스트맨으로 웹소켓 테스트 통과

# from dataclasses import dataclass


# @dataclass
# class ConnectionManager:
#     def __init__(self) -> None:
#         self.active_connections: dict = {}

#     async def connect(self, websocket: WebSocket):
#         await websocket.accept()
#         id = str(uuid.uuid4())
#         self.active_connections[id] = websocket

#         await self.send_message_to(websocket, json.dumps({"type": "connect", "id": id}))

#     def disconnect(self, websocket: WebSocket):
#         id = self.find_connection_id(websocket)
#         del self.active_connections[id]
#         return id

#     def find_connection_id(self, websocket: WebSocket):
#         val_list = list(self.active_connections.values())
#         key_list = list(self.active_connections.keys())
#         id = val_list.index(websocket)
#         return key_list[id]

#     async def send_message_to(self, ws: WebSocket, message: str):
#         await ws.send_text(message)

#     async def broadcast(self, message: str):
#         for connection in self.active_connections.values():
#             await connection.send_text(message)


# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from dataclasses import dataclass
# import uuid
# import json


# @dataclass
# class ConnectionManager:
#     def __init__(self) -> None:
#         self.active_connections: dict = {}

#     async def connect(self, websocket: WebSocket):
#         await websocket.accept()
#         id = str(uuid.uuid4())
#         self.active_connections[id] = websocket

#         await self.send_message_to(websocket, json.dumps({"type": "connect", "id": id}))

#     def disconnect(self, websocket: WebSocket):
#         id = self.find_connection_id(websocket)
#         del self.active_connections[id]
#         return id

#     def find_connection_id(self, websocket: WebSocket):
#         val_list = list(self.active_connections.values())
#         key_list = list(self.active_connections.keys())
#         id = val_list.index(websocket)
#         return key_list[id]

#     async def send_message_to(self, ws: WebSocket, message: str):
#         await ws.send_text(message)

#     async def broadcast(self, message: str):
#         for connection in self.active_connections.values():
#             await connection.send_text(message)


# app = FastAPI()

# connection_manager = ConnectionManager()


# @app.websocket("/messaging")
# async def websocket_endpoint(websocket: WebSocket):
#     # Accept the connection from the client
#     await connection_manager.connect(websocket)
#     try:
#         while True:
#             # Receive the message from the client
#             data = await websocket.receive_text()
#             print("Received: ", data)
#             # Send the message to all the clients
#             await connection_manager.broadcast(data)

#     except WebSocketDisconnect:
#         # Remove the connection from the list of active connections
#         id = connection_manager.disconnect(websocket)
#         # Broadcast the disconnection of client with id to all the clients
#         await connection_manager.broadcast(
#             json.dumps({"type": "disconnected", "id": id})
#         )
