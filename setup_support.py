import os, json

dir_path = os.path.dirname(os.path.realpath(__file__))

class Setup:

    def __init__(self):
        self.db = None
        self.gpio_list = []
        self.mqtt_value = []
        self.is_db_exist = False
        self.db_integrity = False

    def check_if_db_exist(self):
        try:
            self.db = json.load(open("db.json"))
            self.is_db_exist = True
        except:
            pass

    def gpio_setup(self):
        while True:
            name = input("Enter the name: ")
            pin = input("Enter GPIO pin: ")
            location = input("Enter location: ")

            continu = input("Do you want to add more switches (y/n): ")

            self.gpio_list.append({"name": name, "pin": pin, "location": location})

            if continu.upper() == "N":
                break

    def mqtt_setup(self):
        broker_url = input("Enter broker url(default: io.adafruit.com):", "io.adafruit.com")
        port = input("Enter the port(default: 1883): ", "1883")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        refresh_time = input("Enter the refresh time(default 1): ", "1")

        self.mqtt_value = {"broker": broker_url, "port": port, "username": username, "password": password, "refresh_time": refresh_time}

    def create_db(self):
        print("GPIO support")
        self.gpio_setup()
        print("MQTT support")
        self.mqtt_setup()

        with open('db.json', 'w') as outfile:
            json.dump({"gpio": self.gpio_list, "mqtt": self.mqtt_value}, outfile)

        print("DB setup complete")

    def setup_init(self):
        print("DB check")
        self.check_if_db_exist()
        print("DB check completed")
        if not self.is_db_exist:
            self.create_db()



set = Setup()

set.setup_init()
