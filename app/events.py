import aio_pika
import json
from app.config import settings

class EventPublisher:
    def __init__(self):
        self.connection = None
        self.channel = None
    
    async def connect(self):
        """RabbitMQ-ya qoşul"""
        self.connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
        self.channel = await self.connection.channel()
    
    async def publish_event(self, event_type: str, event_data: dict):
        """Event publish et"""
        if not self.channel:
            await self.connect()
        
        exchange = await self.channel.declare_exchange(
            "wishlist_events", 
            aio_pika.ExchangeType.TOPIC,
            durable=True
        )
        
        message_body = json.dumps({
            "event_type": event_type,
            "data": event_data
        })
        
        message = aio_pika.Message(
            body=message_body.encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT
        )
        
        await exchange.publish(
            message,
            routing_key=event_type
        )
    
    async def close(self):
        """Connection bağla"""
        if self.connection:
            await self.connection.close()

# Global event publisher instance
event_publisher = EventPublisher()