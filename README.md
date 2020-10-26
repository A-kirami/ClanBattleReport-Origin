# ClanBattleReport-Origin
本项目基于[@shewinder](https://github.com/shewinder)和[@mahosho](https://github.com/mahosho)的[hoshino](https://github.com/Ice-Cirno/HoshinoBot)插件``retire``(离职报告)，获取[Yobot](https://github.com/pcrbot/yobot)数据生成当期会战报告书

## 特别注意
本仓库已**停止更新**，仅作**留档**用  
建议使用[新版公会战报告书](https://github.com/A-kirami/ClanBattleReport)

### 你应注意
1. ClanBattleReport有不同的风格模板，底图与代码需配套使用
2. 需要hoshino V2版本

### 如何使用
0. 使用前请确认yobot的API访问已开启（默认开启，如果你关闭了api访问，请重新启用）
1. 在``clanbattlereport``中，选取一个主题文件夹，将其重命名为``clanbattlereport``，然后删去其余主题文件夹
2. 将``clanbattlereport``文件夹放入``hoshino``的``modules``文件夹
3. 安装依赖``pandas``
4. 为``matplotlib``安装中文字体(Windows系统可以跳过此步骤)，linux系统使用``pip show matplotlib``找到``matplotlib``的安装位置，并将``msyh.ttf``文件复制到``matplotlib/mpl_data``的``font目录``下
5. [**插件版跳过此步骤**]在``__init__.py``里修改链接到的``yobotapi地址``
6. [**插件版跳过此步骤**]在``data_source.py``里修改``yobot的数据库路径``，**linux系统请确认相关文件的访问权限问题**
7. 修改``config.py``，在``MODULES_ON``中添加``clanbattlereport``

**正确的文件目录结构应为**
```
└── modules
      └──clanbattlereport
              └──clanbattlereport
                        ├─__init__.py
                        ├─data_source.py
                        ├─字体文件
                        └─模板图片
```

### 功能指令
**生成离职报告**
> 生成自己的离职报告书

**生成会战报告**
> 生成自己的本期会战报告书

**看看报告@某人**
> 查看他人的会战报告书（需要群管理权限）

### 当前主题
<details>
<summary>KokoroReport可可萝报告</summary>
<img src="https://i.loli.net/2020/08/09/DKysZJFr3RXlIWL.jpg" width="35%"><img src="https://i.loli.net/2020/08/09/KyzeSGC6JFLNmBv.jpg" width="35%">
</details>
<details>
<summary>PrincessHoliday公主假日</summary>
<img src="https://i.loli.net/2020/08/09/QgR2pNCMAT6BhOI.jpg" width="35%"><img src="https://i.loli.net/2020/08/09/uYPsrHERLFTOGa9.jpg" width="35%">
</details>
