# Windows 10 Anconda python3.8
# coding=utf-8
'''
Author       : LiAo
Date         : 2022-07-06 14:50:02
LastEditTime : 2022-07-12 23:40:46
LastAuthor   : LiAo
Description  : Please add file description
'''

import argparse
import os
from src import bicubic_train, bilinear_train, lanczos_train
os.environ["CUDA_VISIBLE_DEVICES"] = '0'


def bicubic_train_main():
    parser = argparse.ArgumentParser()
    # 网络模型参数
    parser.add_argument('--backbone', type=str, default='tf_efficientnetv2_b2')
    parser.add_argument('--backbone_pretrain', type=bool, default=True)
    parser.add_argument('--pool', type=bool, default=False)
    parser.add_argument('--pool_size', type=tuple, default=(320, 320))
    parser.add_argument('--pool_type', type=str,
                        default='avg', help='must one of (max, avg)')
    parser.add_argument('--weight_decay', type=float, default=0.00)
    # 分类数目
    parser.add_argument('--num_classes', type=int, default=3)

    # 训练epoch
    parser.add_argument('--epoch', type=int, default=100)
    # 超参数, 依据显存设置
    parser.add_argument('--batch_size', type=int,
                        default=16, help='decide by GPU RAM')
    # 学习率参数
    parser.add_argument('--lr', type=float, default=0.005)
    parser.add_argument('--lrf', type=float, default=0.005)

    # 数据集所在目录
    parser.add_argument('--dataset', type=str,
                        default='/data/liao/datasets/cqu_2021_abnormal/')
    # 权重加载路径
    parser.add_argument('--load_weight_path', type=str, default=None)
    # 数据保存的路径
    parser.add_argument('--weight_path', type=str,
                        default='/data/liao/code/apm/result/bicubic/weight/')
    parser.add_argument('--log_path', type=str,
                        default='/data/liao/code/apm/result/bicubic/log/')
    parser.add_argument('--model', type=str, default='apm')
    parser.add_argument('--result_path', type=str,
                        default='/data/liao/code/apm/result/bicubic/result/')

    parser.add_argument('--device', default='cuda',
                        help='device id(i.e. 0 or 0, 1 or cpu)')

    opt = parser.parse_args(args=[])

    # 执行训练和测试
    bicubic_train.main(opt)


def bilinear_train_main():
    parser = argparse.ArgumentParser()
    # 网络模型参数
    parser.add_argument('--backbone', type=str, default='tf_efficientnetv2_b2')
    parser.add_argument('--backbone_pretrain', type=bool, default=True)
    parser.add_argument('--pool', type=bool, default=False)
    parser.add_argument('--pool_size', type=tuple, default=(320, 320))
    parser.add_argument('--pool_type', type=str,
                        default='avg', help='must one of (max, avg)')
    parser.add_argument('--weight_decay', type=float, default=0.00)
    # 分类数目
    parser.add_argument('--num_classes', type=int, default=3)

    # 训练epoch
    parser.add_argument('--epoch', type=int, default=100)
    # 超参数, 依据显存设置
    parser.add_argument('--batch_size', type=int,
                        default=16, help='decide by GPU RAM')
    # 学习率参数
    parser.add_argument('--lr', type=float, default=0.005)
    parser.add_argument('--lrf', type=float, default=0.005)

    # 数据集所在目录
    parser.add_argument('--dataset', type=str,
                        default='/data/liao/datasets/cqu_2021_abnormal/')
    # 权重加载路径
    parser.add_argument('--load_weight_path', type=str, default=None)
    # 数据保存的路径
    parser.add_argument('--weight_path', type=str,
                        default='/data/liao/code/apm/result/bilinear/weight/')
    parser.add_argument('--log_path', type=str,
                        default='/data/liao/code/apm/result/bilinear/log/')
    parser.add_argument('--model', type=str, default='apm')
    parser.add_argument('--result_path', type=str,
                        default='/data/liao/code/apm/result/bilinear/result/')

    parser.add_argument('--device', default='cuda',
                        help='device id(i.e. 0 or 0, 1 or cpu)')

    opt = parser.parse_args(args=[])

    # 执行训练和测试
    bilinear_train.main(opt)


def lanczos_train_main():
    parser = argparse.ArgumentParser()
    # 网络模型参数
    parser.add_argument('--backbone', type=str, default='tf_efficientnetv2_b2')
    parser.add_argument('--backbone_pretrain', type=bool, default=True)
    parser.add_argument('--pool', type=bool, default=False)
    parser.add_argument('--pool_size', type=tuple, default=(320, 320))
    parser.add_argument('--pool_type', type=str,
                        default='avg', help='must one of (max, avg)')
    parser.add_argument('--weight_decay', type=float, default=0.00)
    # 分类数目
    parser.add_argument('--num_classes', type=int, default=3)

    # 训练epoch
    parser.add_argument('--epoch', type=int, default=100)
    # 超参数, 依据显存设置
    parser.add_argument('--batch_size', type=int,
                        default=16, help='decide by GPU RAM')
    # 学习率参数
    parser.add_argument('--lr', type=float, default=0.005)
    parser.add_argument('--lrf', type=float, default=0.005)

    # 数据集所在目录
    parser.add_argument('--dataset', type=str,
                        default='/data/liao/datasets/cqu_2021_abnormal/')
    # 权重加载路径
    parser.add_argument('--load_weight_path', type=str, default=None)
    # 数据保存的路径
    parser.add_argument('--weight_path', type=str,
                        default='/data/liao/code/apm/result/lanczos/weight/')
    parser.add_argument('--log_path', type=str,
                        default='/data/liao/code/apm/result/lanczos/log/')
    parser.add_argument('--model', type=str, default='apm')
    parser.add_argument('--result_path', type=str,
                        default='/data/liao/code/apm/result/lanczos/result/')

    parser.add_argument('--device', default='cuda',
                        help='device id(i.e. 0 or 0, 1 or cpu)')

    opt = parser.parse_args(args=[])

    # 执行训练和测试
    lanczos_train.main(opt)


if __name__ == '__main__':
    bicubic_train_main()
    bilinear_train_main()
    lanczos_train_main()
