import logging



log_file = "/log/logger.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
log_stderr = logging.StreamHandler(sys.stderr)
log_stderr.setLevel(logging.ERROR)
logger = logging.getLogger(__name__)
logger.addHandler(log_stderr)
logging.getLogger("urllib3").setLevel(logging.WARNING)




logger.info("finished the process: {}".format(process))




logger.exception("Failed {}".format(exception))
