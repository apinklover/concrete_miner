from pynput.mouse import Button as B, Controller
import keyboard
import time as t

mouse = Controller()
halt_key = "ctrl"
num_items_per_hotbar = 64

def click(button, for_how_long):
    mouse.press(button)
    t.sleep(for_how_long)
    mouse.release(button)


def place():
    mouse.press(B.right)
    mouse.release(B.right)


def mine():
    click(B.left, 0.75)


def move_down_hotbar(num):
    mouse.scroll(0, num)


def move_up_hotbar(num):
    mouse.scroll(0, -num)


def mine_concrete():
    for hotbar in range(2, 11):
        for i in range(num_items_per_hotbar + 3):      # mines a bit more to account for missed blocks due to lag
            if keyboard.is_pressed(halt_key):
                exit(0)
            place()
            t.sleep(0.05)
            mine()
            t.sleep(0.05)
        try:
            keyboard.press_and_release(f"{hotbar}")
        except ValueError:
            pass
        t.sleep(0.05)
        keyboard.press_and_release("F")
        t.sleep(0.05)
        keyboard.press_and_release("1")
        t.sleep(0.05)

print("hold the pickaxe in the main hand, in hotbar slot 1.\nhold powder in the off-hand.\nfill "
      "the rest of the hotbar slots with powder.\npress CONTROL to exit script.")
dummy = input("when done, press [enter]")
print("executing in 5 seconds.")
t.sleep(5)

mine_concrete()
