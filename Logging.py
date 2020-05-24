def Logging_Notebook(log_name):

  #importing module 
  import logging, logging.handlers
  import time
  from pytz import timezone, utc

  def customTime(*args):
      utc_dt = utc.localize(datetime.utcnow())
      my_tz = timezone("Asia/Kolkata")
      converted = utc_dt.astimezone(my_tz)
      return converted.timetuple()

  logging.Formatter.converter = customTime
  logger.error("customTime")

  ##Creating and Configuring logger
  fhandler = logging.FileHandler(filename=notebook_name, mode='a')
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  fhandler.setFormatter(formatter)
  #logging.Formatter.converter = time.gmtime

  #Setting the threshold of logger to DEBUG 
  logger.addHandler(fhandler)
  logger.setLevel(logging.DEBUG)
  return logger


"""
Usage Example:
notebook_name = "Logging For the Code1.log"
logger_info = Logging_Notebook(notebook_name)
#Test messages 
logger_info.info("\n---------- Logging Started ----------") 
logger_info.debug("Harmless debug Message") 
logger_info.info("Just an information") 
logger_info.warning("Its a Warning") 
logger_info.error("Did you try to divide by zero") 
logger_info.critical("This is critical error") 
"""
