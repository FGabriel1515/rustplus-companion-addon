import asyncio
from rustplus import RustPlusClient

async def main():
    client = RustPlusClient("ip_da_sua_base", 28036, "seu_token_de_acesso")

    await client.connect()

    # Exemplo de assinatura de evento
    @client.on('playerAttack')
    async def on_attack(data):
        print("Base está sendo atacada!")
        # Aqui você pode acionar o Home Assistant via API HTTP, MQTT etc.

    await client.listen()

if __name__ == "__main__":
    asyncio.run(main())
