import configparser
import os

def interpolationDemo(path):
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    print(config.get("Settings", "font_info"))

    print(config.get("Settings", "font_info",
                     vars={"font": "Arial", "font_size": "100"}))


if __name__ == "__main__":
    path = "code_pack_17/2_configparser/settings.ini"
    interpolationDemo(path)