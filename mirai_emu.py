'''
感染
    MiraiバイナリをTFTP経由でダウンロード
    自身をメモリにロード、自身を削除
    C&Cサーバに接続し攻撃司令を待つ
感染後
    Killerプロセス (感染ホストのバイナリを探索し、競合のマルウェアを削除)
    22 (ssh),23 (telnet),80(http)ポートで動作しているサービスをすべて終了させ、それらを自身が参照
    SYN-scanをIPv4アドレス空間からランダムに行い、重み付けした辞書攻撃を行う
    攻撃に成功するとScan Receiverに認証情報を通知

コーディング内容
・コードをTFTP経由でダウンロード
・疑似C&Cサーバに接続
・他のバイナリを探索
・他の機器 (IPアドレスは特定の機器に固定)に辞書攻撃
'''