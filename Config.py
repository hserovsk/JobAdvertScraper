from configparser import ConfigParser

config = ConfigParser()

config["EMAIL"] = {
    "toAddress": "cos@wp.pl",
    "ccAddress": "test"
}

config["PATHS"] = {

}
config["GOOGLE"] = {

}
config["CREDENTIALS"] = {

}

with open("JobAdvertScraper_config.ini", "w") as f:
    config.write(f)