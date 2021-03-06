# Windows 10 Anconda python3.8
# coding=utf-8
'''
Author       : LiAo
Date         : 2022-07-10 23:33:50
LastEditTime : 2022-07-12 09:30:38
LastAuthor   : LiAo
Description  : Please add file description
'''
import argparse
import os
from src import apm_res_train
os.environ["CUDA_VISIBLE_DEVICES"] = '1'

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # 网络模型参数
    parser.add_argument('--backbone', type=str, default='tf_efficientnetv2_b2')
    parser.add_argument('--backbone_pretrain', type=bool, default=True)
    parser.add_argument('--pool', type=bool, default=False)
    parser.add_argument('--pool_size', type=tuple, default=(320, 320))
    parser.add_argument('--pool_type', type=str,
                        default='avg', help='must one of (max, avg)')
    parser.add_argument('--weight_decay', type=float, default=1e-5)
    # 分类数目
    parser.add_argument('--num_classes', type=int, default=3)

    # 训练epoch
    parser.add_argument('--epoch', type=int, default=100)
    parser.add_argument('--epoch_offset', type=int, default=0)
    # 超参数, 依据显存设置
    parser.add_argument('--batch_size', type=int,
                        default=16, help='decide by GPU RAM')
    # 学习率参数
    parser.add_argument('--lr', type=float, default=0.005)
    # used for RangeLars
    parser.add_argument('--lrf', type=float, default=0.005)

    # 数据集所在目录
    parser.add_argument('--dataset', type=str,
                        default='/data/liao/datasets/cqu_2021_abnormal/')
    # 权重加载路径
    parser.add_argument('--load_weight_path', type=str,
                        default=None)  # /data/liao/code/apm/result/apm/weight/best_weight.pth
    # 数据保存的路径
    parser.add_argument('--weight_path', type=str,
                        default='/data/liao/code/apm/result/apm_res/weight/')
    parser.add_argument('--log_path', type=str,
                        default='/data/liao/code/apm/result/apm_res/log/')
    parser.add_argument('--model', type=str, default='apm')
    parser.add_argument('--result_path', type=str,
                        default='/data/liao/code/apm/result/apm_res/result/')

    parser.add_argument('--device', default='cuda',
                        help='device id(i.e. 0 or 0, 1 or cpu)')

    opt = parser.parse_args(args=[])

    # 执行训练和测试
    apm_res_train.main(opt)
