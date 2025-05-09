import machine
import utime
def blink(led_pin, interval):
    """
    指定したLEDを interval 秒 点滅させる関数
    """
    led_pin.value(1)
    utime.sleep(interval)
    led_pin.value(0)
    utime.sleep(interval)
def main():
    blink_interval = 0.5
    led = machine.Pin(0, machine.Pin.OUT)

    while True:
     blink(led, blink_interval)

if __name__ == "__main__":
    main()
