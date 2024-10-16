# -*- coding: utf-8 -*-
import logging

# 设置日志格式，包含时间、日志等级和消息
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
    level=logging.INFO  # 日志级别
)

logger = logging.getLogger(__name__)

logger.info("cron_task...")
