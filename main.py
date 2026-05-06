import uasyncio as asyncio
import gc

async def main(zbot):
    gc.collect()
    servo = zbot.servo(2)
    drive = zbot.motor(1)
    centerAngle = 20


    async def forward(power):
        servo.angle(centerAngle)
        await asyncio.sleep_ms(250)
        drive.on(power)

    async def stop():
        drive.off()
        await asyncio.sleep_ms(250)


    servo.angle(centerAngle)

    while True:

        # await forward(-100)
        # asyncio.sleep_ms(2000)
        # await stop()
        zbot.display("yo",centerAngle)
        await asyncio.sleep_ms(2000)
        for i in range(100):
            zbot.display("yo",i)
            asyncio.sleep_ms(100)
        # forward(-100)
        zbot.display("yo 1",centerAngle)

