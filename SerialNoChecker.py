# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 11:59:35 2015

@author: victor
"""
 
def company_serial_no_checker(serial):
    # 共八位，全部為數字型態
    if len(serial)!=8 or not serial.isdigit():
        return False
    
    # 各數字分別乘以 1,2,1,2,1,2,4,1
    # 例：統一編號為 53212539
    #
    # Step1 將統編每位數乘以一個固定數字固定值
    #   5   3   2   1   2   5   3   9
    # x 1   2   1   2   1   2   4   1
    # ================================
    #   5   6   2   2   2  10  12   9
    #
    
    serial_list = list(serial)
    coeff = [1, 2, 1, 2, 1, 2, 4, 1]
    
    # print serial_list

    # Define a list with 8 zeros    
    multiple = [0]*8
    
    count = 0
    while count < 8:
        # print count
        temp = int(serial_list[count])*coeff[count]
        multiple[count] = temp if temp < 10 else (temp/10) + (temp % 10)
        count = count + 1
    
    # Step2 將所得值取出十位數及個位數
    # 十位數 個位數
    #   0      5
    #   0      6
    #   0      2
    #   0      2
    #   0      2
    #   1      0
    #   1      2
    #   0      9
    #
    # 並將十位數與個位數全部結果值加總
    #
   
    total = sum(multiple)
    
    # Step3 判斷結果
    # 第一種:加總值取10的餘數為0
    # 第二種:加總值取10的餘數等於9而且統編的第6碼為7
    
    if (total % 10 == 0):
        return True
    elif ((total + 1) % 10 == 0 and serial[5] == '7'):
        return True
    else:
        return False

if __name__=='__main__':
    # 位數不足
    #print company_serial_no_checker('5312539')   # false
     
    # 符合
    #print company_serial_no_checker('53212539')  # true
     
    # 不符合
    #print company_serial_no_checker('12222539')  # nil, 在邏輯判斷的時候也會被當false
    
    print company_serial_no_checker('27206130')
    
    