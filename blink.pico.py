import machine
import utime
try:
     blink_interval = float(input("点滅感覚（秒）を入力してください："))
except ValueError:
     print("無効な入力です。デフォルトの0.5秒にします。")
     blink_interval = 0.5
led = machine.Pin(0, machine.Pin.OUT)
while True:
     led.value(1)
     utime.sleep(blink_interval)
     led.value(0)
     utime.sleep(blink_interval)