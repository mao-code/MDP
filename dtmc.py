# 實作馬卡夫鏈/離散時間馬可夫鏈(DTMC -> Discrete-Time Markov Chain)
# source: https://ithelp.ithome.com.tw/articles/10201028

import numpy as np

# 定義轉移矩陣 define transition matrix
Matrix_trans = np.array([[0.9, 0.1], [0.5, 0.5]])

# afer n steps
Matrix_trans_step3 = np.linalg.matrix_power(Matrix_trans, 3)
Matrix_trans_step5 = np.linalg.matrix_power(Matrix_trans, 5)
Matrix_trans_step10 = np.linalg.matrix_power(Matrix_trans, 10)
Matrix_trans_step50 = np.linalg.matrix_power(Matrix_trans, 50)
Matrix_trans_step100 = np.linalg.matrix_power(Matrix_trans, 100)

# print result -> 確認其會收斂
# print('After 3 steps: \n', Matrix_trans_step3, '\n')
# print('After 5 steps: \n', Matrix_trans_step5, '\n')
# print('After 10 steps: \n', Matrix_trans_step10, '\n')
# print('After 50 steps: \n', Matrix_trans_step50, '\n')
# print('After 100 steps: \n', Matrix_trans_step100, '\n')

# set init state s0
# s0 = np.array([1.0, 0.0])

# print result
# print('Init state: \n', s0, '\n')
# print('After 3 steps: \n', np.dot(s0, Matrix_trans_step3), '\n')
# print('After 5 steps: \n', np.dot(s0, Matrix_trans_step5), '\n')
# print('After 10 steps: \n', np.dot(s0, Matrix_trans_step10), '\n')
# print('After 50 steps: \n', np.dot(s0, Matrix_trans_step50), '\n')
# print('After 100 steps: \n', np.dot(s0, Matrix_trans_step100), '\n')

# random init state
rand_num = np.random.rand(1) # 1 shape ndarray -> [rand]
random_s0 = np.array([rand_num, 1-rand_num]).reshape(2)

# print result
print('Init state: \n', random_s0, '\n')
print('After 3 steps: \n', np.dot(random_s0, Matrix_trans_step3), '\n')
print('After 5 steps: \n', np.dot(random_s0, Matrix_trans_step5), '\n')
print('After 10 steps: \n', np.dot(random_s0, Matrix_trans_step10), '\n')
print('After 50 steps: \n', np.dot(random_s0, Matrix_trans_step50), '\n')
print('After 100 steps: \n', np.dot(random_s0, Matrix_trans_step100), '\n')