# yolo_convert4keras-yolo
labelImageで作ったアノテーションファイルがkeras-yoloと互換性なかったので変換スクリプト作りました

python3 yolo_convert4keras-yolo.py [アノテーションファイルをまとめたディレクトリパス（/は要りません）] [入力画像のwidth] [入力画像のheight]
出力：train.txt

画像のパスは"./img/XXXX.jpg"になるので適宜書き換えて使ってください
