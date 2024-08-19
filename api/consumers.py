import json
from channels.generic.websocket import AsyncWebsocketConsumer

class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_addi(
            "orders_group",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "orders_group",
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            "orders_group",
            {
                'type': 'order_status_update',
                'message': message
            }
        )

    async def order_status_update(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))