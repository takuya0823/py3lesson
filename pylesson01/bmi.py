# coding: Shift_JIS
__author__ = 'ts'

while True:
    height = input('�g��(��)?:')
    if len(height) == 0:
        break
    height = float(height)                      #�����ɕϊ�
    weight = float(input('�̏d(kg)?:'))
    bmi = weight/pow(height,2)                  #�g�ݍ��݊֐�pow�ŗݏ�v�Z
    print('BMI�l��%0.1f�ł��B' % bmi)         #�����_���ʂ܂ł̏o��
    if bmi < 18.5:
        print('�������������ł�')
    elif 18.5 <= bmi < 25.0:
        print('�W���I�ȑ̌^�ł�')
    elif 25.0<= bmi < 30:
        print('���������Ă��܂�')
    else:
        print('���x�̔얞�ł�')