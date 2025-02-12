from ncatbot.plugin.loader import BasePlugin, CompatibleEnrollment
from ncatbot.core.message import GroupMessage

bot = CompatibleEnrollment  # 兼容回调函数注册器

class MyPlugin(BasePlugin):
    name = "MyPlugin" # 插件名称
    version = "0.0.1" # 插件版本

    @bot.group_event()
    async def on_group_event(self, msg: GroupMessage):
        # 定义的回调函数
        if msg.raw_message == "测试":
            await self.api.post_group_msg(msg.group_id, text="Ncatbot 插件测试成功喵")

    async def on_load(self):
        # 插件加载时执行的操作, 可缺省
        print(f"{self.name} 插件已加载")
        print(f"插件版本: {self.version}")