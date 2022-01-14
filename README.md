# robosys2021_ros_program
ロボットシステム学の第2課題で作成
小倉百人一首リストを作りました

# 概要
小倉百人一首のリストをROSによって表示する

1~100首、すべて入っています

# 実装内容
- Publisherを起動している端末で1~100の数字を打ち込む
- 1~100に対応した首がSubscriberを起動している端末に表示される

# 実装環境
- RaspberryPi4B
- Ubuntu20.04
- ros noetic

# 実装手順
1. インストール
```
$cd ~/catkin_ws/src
$git clone https://github.com/Takehiro-Hasegawa/robosys2021_ros_program.git
```
2. パッケージのビルド
```
$cd ~/catkin_ws
$catkin_make
```

# 参考URL

https://techacademy.jp/magazine/36666
