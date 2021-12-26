### 疲劳驾驶检测系统

此项目通过使用PaddleDetection+PaddleLite部署（方案1）及Paddle2onnx转IR的OpenVINO部署（方案2），实现了通过驾驶员的眼部、嘴部动作推断疲劳状态，使得驾驶员能实时被本地语音方式提醒，同时后台管理人员能接收到司机疲劳报警信息。

#### 依赖：

此项目运行依赖 `MySQL` 数据库，请安装数据库并加载备份文件后再执行本程序，具体操作可参照 [*MySQL* 教程 | 菜鸟教程](https://www.runoob.com/mysql/mysql-tutorial.html))

数据库备份文件：`./sql_backups/20211226204206.nb3`

#### 项目环境：

Python >= 3.7

#### 数据集：

本项目所用数据集来自 [AIStudio公开数据集：疲劳驾驶行为数据集](https://aistudio.baidu.com/aistudio/datasetdetail/106856)

#### 快速开始：

```shell
pip install -r requirements.txt
```
- PC端执行：

  ```shell
  python main.py
  ```
  
- 移动端执行：

  ```shell
  python arm_main.py
  ```

  

