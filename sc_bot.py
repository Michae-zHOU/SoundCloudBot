import sys
import time
from helper import *
from constant import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class SoundCloudBot:
    def __init__(self, count, url):
        self.count = count
        self.url = url
        self.stop_time = 0
        self.prev_play_count = 0
        self.curr_play_count = 0
        self.stable_count = 0

    def run(self):
        for cur_run in range(self.count):
            self.__print_run(cur_run)
            self.one_run()

    def one_run(self):
            self.__start()
            self.__wait_till_ready()
            self.__mute()
            self.__play()
            self.__print_play_count()
            self.__wait_for_sc_server_to_update()
            self.__pause()
            self.__close()

    def __print_run(self, cur_run):
            decorater = "=" * 50
            print("\n\n\n")
            print(decorater + " Current Run: " + str(cur_run + 1) + " " + decorater)

    def __start(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)

    def __wait_till_ready(self):
        try:
            element_present = EC.presence_of_element_located((By.XPATH, PLAY_BUTTON_XPATH))
            WebDriverWait(self.driver, LOADING_TIMEOUT).until(element_present)
            print("Play button loaded.")
        except TimeoutException:
            print("Timed out waiting for page to load.")

        try:
            element_present = EC.presence_of_element_located((By.XPATH, VOLUME_BUTTON_XPATH))
            WebDriverWait(self.driver, LOADING_TIMEOUT).until(element_present)
            print("Volume button loaded.")
        except TimeoutException:
            print("Timed out waiting for page to load.")

    def __mute(self):
        self.volume_button = self.driver.find_element(By.XPATH, VOLUME_BUTTON_XPATH)
        self.volume_button.click()

    def __play(self):
        self.play_button = self.driver.find_element(By.XPATH, PLAY_BUTTON_XPATH)
        self.play_button.click()
        time.sleep(PLAY_TIME)
    
    def __print_play_count(self):
        play_count_tab = self.driver.find_element(By.XPATH, PLAY_TAB)
        print("Current track played count: " + play_count_tab.text)
        self.curr_play_count = get_number_from_str(play_count_tab.text)
    
    def __wait_for_sc_server_to_update(self):
        if not ENABLE_WAIT:
            return
        if self.prev_play_count >= self.curr_play_count:
            self.stop_time += 1
            self.stable_count = 0
            time.sleep(self.stop_time)
        else:
            self.stable_count += 1

        if self.stable_count >= STABLE_THRESH_HOLD and self.stop_time > 0:
            self.stop_time -= 1

        print("Play time extends by " + str(self.stop_time) + " seconds.")
        self.prev_play_count = self.curr_play_count

    def __pause(self):
        self.pause_button = self.driver.find_element(By.XPATH, PLAY_BUTTON_XPATH)
        self.pause_button.click()
        time.sleep(PAUSE_TIME)

    def __close(self):
        self.driver.quit()

def main():
    run_count = DEFAULT_RUN
    url = DEFAULT_URL
    if len(sys.argv) > 1:
        run_count = int(sys.argv[1])
    if len(sys.argv) > 2:
        url = sys.argv[2]
    print("Run: " + str(run_count))
    print("Url: " + url)

    bot = SoundCloudBot(run_count, url)
    bot.run()

if __name__ == "__main__":
    main()