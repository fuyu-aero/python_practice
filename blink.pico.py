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
    blink_history = []

    while True:
        blink(led, blink_interval)
        blink_history.append(blink_interval)

        # 5回ごとに履歴を表示
        if len(blink_history) % 5 == 0:
            print("履歴:", blink_history)
if __name__ == "__main__":
    main()
