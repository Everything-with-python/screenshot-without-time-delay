import pyautogui
import time

time.sleep(3)
ss = pyautogui.screenshot()
ss.save("screenshot 2.png")

# u can change the time (in seconds) for ur wish
# here i used to wait for 3sec, so after 3sec it will take a screenshot
# u can save the screenshot name by giving within the double quotes like the last line of the code
