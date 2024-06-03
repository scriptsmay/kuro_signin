# Kuro-autosignin
python脚本库街区论坛及游戏自动签到
库街区 游戏及库洛币自动签到

## 使用说明

1. **替换个人信息**：请替换脚本中的 `token`、`devcode` 和 `distinct_id`。
2. **获取 Token**：使用 `tools.py` 来获取你的 `token`。
3. **已对接server酱**: 替换 `sckey`


## 青龙配置

### 1.拉取仓库

指令拉取

```sh
ql repo https://github.com/scriptsmay/kuro_signin.git "run.py" "" ".py|requirements"
```

### 2.环境变量添加

在青龙面板环境变量中添加以下变量

| 名称                    | 值                           | 功能                    |
|-------------------------|-----------------------------|------------------------|
| KURO_CONFIG_PATH        | /ql/config/kuro_config.json | 设置配置文件路径（必选）    |


### 3.复制配置文件

**进入容器后运行以下命令**（docker exec -it ql bash）修改 ql 为你的青龙容器名字

```sh
cp /ql/repo/scriptsmay_kuro_signin/config.sample.json /ql/config/kuro_config.json
```

### 4.添加依赖

schedule
requests
