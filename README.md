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
3. roscoreの起動
```
$roscore
```
4. パーミッション設定
```
$cd ~/catkin_ws/src/robosys2021_ros_program/scripts
$chmod 755 chr.py chrrev.py
```
5. chr.py chrrev.pyの起動
それぞれ別の端末で起動する
```
$rosrun mypkg chr.py
```
```
$rosrun mypkg chrrev.py
```
6. キーボード操作
1~100の数字の内一つをchr.pyの端末に入力しエンターを押す
7. 表示
chrrev.pyに句が表示される

# 動画
実行中の動画です
https://youtu.be/OkopgMPOhX0
＊動画では10首までだしています
# 参考URL

https://techacademy.jp/magazine/36666


https://qiita.com/keinko/items/7d0f26c19414291660d9
