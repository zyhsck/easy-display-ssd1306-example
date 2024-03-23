# 这是一个使用示例 This is an example of usage
import time
from machine import SPI, Pin,I2C
import ssd1306
from easydisplay import EasyDisplay

# ESP32S3 & ST7735
i2c = I2C(scl=Pin(22), sda=Pin(21))
dp = ssd1306.SSD1306_I2C(width=128, height=64,i2c=i2c)
ed = EasyDisplay(dp, "MONO", font="/text_lite_16px_2312.v3.bmf", show=True, color=0xFFFF, clear=True)


time.sleep(3)
ed.text("我爱你", 0, 0)

