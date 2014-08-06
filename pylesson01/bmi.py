# coding: Shift_JIS
__author__ = 'ts'

while True:
    height = input('身長(ｍ)?:')
    if len(height) == 0:
        break
    height = float(height)                      #小数に変換
    weight = float(input('体重(kg)?:'))
    bmi = weight/pow(height,2)                  #組み込み関数powで累乗計算
    print('BMI値は%0.1fです。' % bmi)         #小数点第一位までの出力
    if bmi < 18.5:
        print('少し痩せすぎです')
    elif 18.5 <= bmi < 25.0:
        print('標準的な体型です')
    elif 25.0<= bmi < 30:
        print('少し太っています')
    else:
        print('高度の肥満です')