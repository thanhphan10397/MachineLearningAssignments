#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# IMPORT
import numpy as np


# In[ ]:


# GRADED FUNCTION
'''
TO_DO_1: Khởi tạo ma trận số thực kích thước M x N gồm toàn số K.
Input:
   - M: kiểu số nguyên, là số hàng của ma trận
   - N: kiểu số nguyên, là số cột của ma trận
   - K: kiểu số nguyên là giá trị của một phần tử cần điền vào ma trận
Output:
   - Kiểu numpy array, chứa ma trận kích thước M x N gồm toàn các giá trị thực K
'''
def matrix_of_K(M, N, K):
    matrix = np.full((M, N), K)
    
    return matrix


# In[1]:


# GRADED FUNCTION
'''
TO_DO_2: Khởi tạo ma trận số thực kích thước M x N gồm các số từ 1 đến M.N 
được sắp tăng từ trái qua phải, từ trên xuống dưới. Ví dụ:
Input: 
   - M: kiểu số nguyên, là số hàng của ma trận
   - N: kiểu số nguyên, là số cột của ma trận
Output:
   - Kiểu numpy array, chứa ma trận kích thước M x N với các phần tử là số thực lần lượt là
   1, 2, 3, ..., MN

Ví dụ: M = 2, N = 3, output là
    array([[1, 2, 3],
           [4, 5, 6]])
'''

def matrix_of_MN(M, N):
    array = np.arange(1, M*N+1).reshape(M,N)
    return array


# In[ ]:


# GRADED FUNCTION
'''
TO_DO_3: Tính số tiền còn lại trong tài khoản ngân hàng với đầu vào là
danh sách các lần gửi tiền và rút tiền
Input:
   - deposits: kiểu numpy array, chứa danh sách các số tiền gửi vào tài khoản
   - withdraws: kiểu numpy array, danh sách các số tiền rút khỏi tài khoản
Output:
   - Kiểu số thực, số tiền còn lại trong tài khoản
Ví dụ: deposits = [100.0, 400.0, 200.0], withdraws = [50.0, 100.0], số tiền còn lại sẽ là: 550

'''
def balance(deposits, withdraws):
    arr = np.sum(deposits) - np.sum(withdraws)
    return arr


# In[ ]:


# GRADED FUNCTION
'''
TO_DO_4: Tính số tiền còn lại trong tài khoản ngân hàng với đầu vào là
danh sách các số tiền giao dịch, tương ứng là sẽ có danh sách
các loại giao dịch gửi tiền (ký hiệu bằng chuỗi 'D'), rút tiền 
(ký hiệu bằng chuỗi 'W')
Input:
   - moneys: kiểu numpy array, chứa danh sách các số tiền giao dịch
   (gửi và rút khỏi tài khoản)
   - types: kiểu numpy array, chứa danh sách các loại giao dịch 
   (gửi ký hiệu là 'D', rút ký hiệu là 'W')
Output:
   - Kiểu số thực, số tiền còn lại trong tài khoản
Ví dụ: moneys = [400.0, 100.0, 200.0], types = ['D', 'W', 'D'], số tiền còn lại sẽ là: 500

'''
def balance2(moneys, types):
    withdraw = 0
    deposit = 0
    for i in range(len(types)):
        if (types[i] == 'W'):
            withdraw += moneys[i]
        else:
            deposit += moneys[i]

    total = deposit - withdraw 
    return total    


# In[ ]:


# GRADED FUNCTION
'''
TO_DO_5: Đếm số lượng sinh viên có điểm số không dưới K điểm cho trước của một lớp học.
Input: 
   - marks: kiểu numpy array, kích thước 1 x n. Đây là điểm toán cả n sinh viên trong lớp.
   - K: kiểu số thực, điểm chuẩn. 
Output: 
   - Kiểu số nguyên, số lượng sinh viên trong lớp đạt từ K điểm trở lên
'''

def pass_exam(marks, K):
    good_marks = marks[np.where(marks >= K)]
    a = len(good_marks)
    return a


# In[ ]:


# GRADED FUNCTION
'''
TO_DO_6: Tính điểm trung bình của một bạn sinh viên biết trước danh sách các điểm số và số tín chỉ
của từng môn học.
Input: 
   - marks: kiểu numpy array, kích thước 1 x n. Đây là điểm các môn của một sinh viên.
   - credits: kiểu numpy array, kích thước 1 x n. Đây là số tín chỉ lần lượt của các môn. 
Output: 
   - Kiểu số thực, điểm trung bình của các môn học của sinh viên

Ví dụ: Điểm trung bình ba môn Toán, Văn, Anh của một sinh viên lần lượt là:
   marks = np.array([8.0, 9.0, 10.0])
   credits = np.array([2,2,1])
   output là: 8.8
'''
def gpa(marks, credits):
    arr = np.array([])
    arr = np.multiply(marks, credits)
    values = np.sum(arr)/ np.sum(credits)
    return values


# In[ ]:


# GRADED FUNCTION
'''
TO_DO_7: Tính điểm trung bình cao nhất của một lớp học biết trước danh sách các điểm số và số tín chỉ
cho từng môn học của một lớp.
Input: 
   - marks: kiểu numpy array, kích thước m x n. Đây là điểm các môn của một lớp học.
   Trong đó, m là số sinh viên, n là số môn học
   - credits: kiểu numpy array, kích thước 1 x n. Đây là số tín chỉ lần lượt của các môn. 
Output: 
   - Kiểu số thực, điểm trung bình của sinh viên cao nhất.

Ví dụ: Điểm trung bình ba môn Toán, Văn, Anh của một lớp học có 5 bạn lần lượt là:
   marks = np.array(
       [[8.0, 9.0, 10.0],
       [7.0, 9.0, 8.0],
       [8.0, 8.0, 8.0],
       [10.0, 9.0, 7.0],
       [9.0, 9.0, 10.0]])
   credits = np.array([2,2,1])
   output là: 9.2
'''
def max_gpa(marks, credits):
    arr = []
    for i in range(len(marks)):
        arr = np.append(arr,np.sum(credits*marks[i]/np.sum(credits)))
    a=np.max(arr)
    return a




# In[ ]:


# GRADED FUNCTION
'''
TO_DO_8: Tính điểm trung bình tích luỹ của từng sinh viên trong lớp học biết trước 
danh sách các điểm số và số tín chỉ cho từng môn học của một lớp. Lưu ý rằng,
khi tính điểm trung bình ta sẽ loại bỏ các điểm của các tín chỉ dưới 5 (rớt).
Input: 
   - marks: kiểu numpy array, kích thước m x n. Đây là điểm các môn của một lớp học.
   Trong đó, m là số sinh viên, n là số môn học
   - credits: kiểu numpy array, kích thước 1 x n. Đây là số tín chỉ lần lượt của các môn. 
Output: 
   - Kiểu numpy array, kích thước 1 x m, chứa điểm trung bình của các bạn sinh viên trong lớp.

Ví dụ: Điểm trung bình ba môn Toán, Văn, Anh của một lớp học có 5 bạn lần lượt là:
   marks = np.array(
       [[8.0, 9.0, 10.0],
       [4.0, 9.0, 8.0],
       [8.0, 3.0, 8.0],
       [10.0, 9.0, 5.0],
       [9.0, 9.0, 4.0]])
   credits = np.array([2,2,1])
   output là: array([8.8, 8.66666667, 8. , 8.6, 9.])
'''
def gpa_of_pass(marks, credits):
    average = np.array([])
    lst_over5 =[]
    lst_over5 = np.where(marks < 5,0,1)
    for i in range(len(lst_over5)):
        average = np.append(average,np.sum((marks[i]*lst_over5[i]*credits)/np.sum(credits*lst_over5[i])))
    return average

