import os

import botpy
from botpy import logging

from botpy.ext.cog_yaml import read

import PcrUtils
from pojo.Rank import Rank

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()
from botpy.message import GroupMessage, Message


class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 启动成功!")

    async def on_group_at_message_create(self, message: Message):
        # messageResult = await message._api.post_group_message(
        #     group_openid=message.group_openid,
        #     msg_type=0,
        #     msg_id=message.id,
        #     content=f"收到了消息：{message.content}")
        _log.info({self.robot.name})
        _log.info({message.content.strip()})
        if (message.content.strip() == "查询当前排名"):
            data = PcrUtils.rank();
            _log.info(type(data.fetch_data()))
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=data.fetch_data()
            )

        if (message.content.strip() == "【更新param】"):
            _log.info(message.content)
            strs = PcrUtils.updateParam().fetch_data(message.content);
            await message.reply(content=strs)
        #
        if(message.content.strip() == "获取更新模板"):
            _log.info(message.content)
            strs = PcrUtils.getUpdateTemplate().fetch_data(message.content);
            await message.reply(content=strs)
        # if
        ##回复消息
        # await message._api.post_group_message(
        #     group_openid=message.group_openid,
        #     msg_type=1,  # 7表示富媒体类型
        #     msg_id=message.id,
        #     media=message.attachments[0].url
        # )

        # message.reply("content:"+message.content +"channel_id"+ message.channel_id+"member"+message.member+"author:"+message.author)
        # _log.info(messageResult)


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], secret=test_config["secret"])
