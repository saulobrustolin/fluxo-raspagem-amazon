import asyncio
import aio_pika
from automation.inpi.access_inpi import access_inpi

async def main():
    connection = await aio_pika.connect_robust("amqp://localhost/")
    channel = await connection.channel()
    
    queue = await channel.declare_queue(
        "brand_name",
        durable=True,
        auto_delete=False
    )

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                await access_inpi(None, None, None, message.body)

print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
asyncio.run(main())
