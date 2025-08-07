# WeChat_Run

注意！本项目必须下载注册**Zepp_life**并绑定微信 账号（Email or phone）和密码 就是你的Zeep_life的账号和密码 `<br>`
使用Python和Github Actions每日定时WeChat（微信）刷步

# 使用 & 配置

## 请先Fork本项目

如下配置完后在Actions启动试试 `<br>`
`Setting - Secrets and variables - Actinos - New repository secret<br>`
Secrets按如下填写：

| Name                  | secret         |
| --------------------- | -------------- |
| ACTION_RUNZEPP_DATA_1 | (填写你的信息) |
| ACTION_RUNZEPP_DATA_2 | (填写你的信息) |
| ACTION_RUNZEPP_DATA_3 | (填写你的信息) |
| ...                   | ...            |

> `ACTION_RUNZEPP_DATA_xx`

```
第一行 账号
第二行 密码
第三行(可选) 最少跑步的数量 如果第三行不写的话，则随机选取一个数值运行
第四行(可选) 最多跑步的数量 不填则默认为第三行的数量
```

注：`PHONE`、`PASSWORD`为必填项，`RUN_START`为最少跑步数量 `<br>`
想在某个数量之间的话请多添加一行 `RUN_END`，最终结果将会在 `RUN`和 `RUN_END`之间 `<br>`
运行时间修改 `.github/workflows/run_zepp.yml`旁边有相关的注释

```bash
  schedule:
  # 定时任务，在每天的05:00执行
    - cron: '0 21 * * *'
```

注意！北京时间比Github所使用时区快8个小时 `<br>`
所以这里的 `- cron: '0 21 * * *'`其实就是 `(21 + 8) % 24 = 5`其中的 5 就是我们时间的早上5点
