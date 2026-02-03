from loguru import logger

# 配置日志输出格式和级别
logger.add(
    sink=lambda msg: print(msg, end=""),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="DEBUG",
)
logger.debug("This is a debug message")
