import logging


class log:

    @staticmethod
    def logs():
        logging.basicConfig(filename=".\Test_Results\Test_logs.log",
                            format='%(asctime)s: - %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
        logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger

