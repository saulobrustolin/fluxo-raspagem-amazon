import asyncio
import aio_pika
from scripts.product.scrapping_product import scrapping  # async def

RABBITMQ_URL = "amqp://localhost/"

async def main():
    # Conexão assíncrona
    connection = await aio_pika.connect_robust(RABBITMQ_URL, heartbeat=60)
    
    async with connection:
        channel = await connection.channel()
        
        # Garante que a fila existe
        queue = await channel.declare_queue("products_link", durable=True)
        
        # Consome mensagens de forma assíncrona
        async with queue.iterator() as queue_iter:
            print(" [*] Aguardando mensagens. Para sair pressione CTRL+C")
            async for message in queue_iter:
                async with message.process():  # ack automático no sucesso
                    try:
                        await scrapping(message)  # sua função scrapping deve ser async e aceitar `message`
                    except Exception as e:
                        print(f"[consumer] Erro ao processar mensagem: {e}")
                        # mensagem não é ackada automaticamente se ocorrer exceção

if __name__ == "__main__":
    asyncio.run(main())
