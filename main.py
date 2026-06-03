import uasyncio as asyncio
from robot.ackermann import AckermannDrive


async def main(zbot):
    drive = AckermannDrive(
        zbot,
        drive_motor_port = 2,
        steering_port = 1,
        center_angle = 90,
        min_angle = 45,
        max_angle = 135,
    )

    drive.steer_center()

    zbot.display("Ackermann", "Forward")
    drive.drive(50, 90)
    await asyncio.sleep_ms(1000)

    drive.stop()
    drive.steer_center()
    zbot.display("Ackermann", "Stopped")

    drive.drive(50, 135)
    await asyncio.sleep_ms(1000)
    drive.stop()

    while True:
        await asyncio.sleep_ms(1000)
