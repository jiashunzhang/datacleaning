import matplotlib.pyplot as plt
import pandas as pd

def plot():
    y_axis = pd.Series([0.161, 0.159, 0.160, 0.157, 0.158, 0.147, 0.142, 0.138, 0.132, 0.12, 0.13, 0.084, 0.065, 0.066, 0.05, 0.04, 0.03, 0.031, 0.033, 0.032, 0.03, 0.031, 0.033, 0.032, 0.031, 0.033, 0.032, 0.03, 0.031, 0.033, 0.032])
    x_axis = range(0, len(y_axis), 1)
    plt.plot(x_axis, y_axis)
    plt.ylabel('包外错误率', fontproperties='SimHei', fontsize=15)
    plt.xlabel('特征子集维度', fontproperties='SimHei', fontsize=15)
    plt.show()


plot()
