import asyncio
import aio_pika
from automation.inpi.access_inpi import access_inpi

async def main():
    connection = await aio_pika.connect_robust("amqp://localhost/")
    channel = await connection.channel()
    
    queue = await channel.declare_queue(
        "brand_name",
        durable=True,       # igual ao existente
        auto_delete=False   # ou True se a fila original for auto_delete
    )

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                await access_inpi(None, None, None, message.body)

asyncio.run(main())
