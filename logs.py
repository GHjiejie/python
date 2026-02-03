# 创建的打印
# 使用内置的logging模块记录日志信息
from logging import getLogger, StreamHandler, Formatter, DEBUG

# 创建一个模块为jiejie的logger对象
logger = getLogger("jiejie")

# 日志输出到控制台
handler = StreamHandler()
# 设置日志输出格式
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 将格式应用到handler，确保输出到控制台时使用该格式
handler.setFormatter(formatter)

# 将handler添加到logger对象
logger.addHandler(handler)

# 设置打印的日志级别为DEBUG，DEBUG以上级别的日志会被打印
logger.setLevel(DEBUG)
logger.debug("This is a debug message")
logger.info("This is an info message")
