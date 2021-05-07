from EngineCKB import Engine

test_str = ["1. Một cửa hàng buổi sáng bán được 13 kg đường. Buổi chiều bán được số đường gấp ba lần số đường bán được vào buổi sáng. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            "2. Một cửa hàng ngày thứ nhất bán được 28 lít dầu. Số dầu ngày thứ hai bán được bằng 1/7 số dầu bán được của ngày thứ nhất. Hỏi cả hai ngày cửa hàng bán được bao nhiêu lít dầu?",
            "3. Mai có 21 nhãn vở, An có nhiều hơn Mai 3 nhãn vở. Hỏi cả hai bạn có tất cả bao nhiêu cái nhãn vở?",
            "4. Mỹ hái được 40 bông hoa. Số bông hoa Linh hái được bằng 1/5 số hoa Mỹ hái được. Hỏi hai bạn hái được tất cả bao nhiêu bông hoa?",
            "5. Một cửa hàng buổi sáng bán được 26 kg đường. Số đường buổi sáng bán được ít hơn số đường bán trong buổi chiều là 26 kg. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            #"6. Trong vườn của bác Nam có 66 cây bưởi, số cây chuối bằng 1/6 số cây bưởi. Hỏi trong vườn nhà bác Nam có bao nhiêu cây bưởi và chuối?",
            "7. Một cửa hàng buổi sáng bán được 17 kg đường. Số đường buổi sáng bán được ít hơn số đường bán trong buổi chiều là 51 kg. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            "8. Một cửa hàng ngày thứ nhất bán được 64 lít dầu. Số dầu ngày thứ hai bán được bằng 1/8 số dầu bán được của ngày thứ nhất. Hỏi cả hai ngày cửa hàng bán được bao nhiêu lít dầu?",
            "9. Một cửa hàng buổi sáng bán được 28 kg đường. Số đường buổi sáng bán được ít hơn số đường bán trong buổi chiều là 12 kg. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            "10. Mỹ hái được 36 bông hoa. Số bông hoa Linh hái được bằng 1/4 số hoa Mỹ hái được. Hỏi hai bạn hái được tất cả bao nhiêu bông hoa?",
            "11. Một cửa hàng buổi sáng bán được 49 kg đường. Số đường buổi sáng bán được nhiều hơn số đường bán trong buổi chiều 32 kg. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            "12. Mỹ hái được 13 bông hoa, Linh hái được nhiều hơn Mỹ 45 bông hoa. Hỏi hai bạn hái được tất cả bao nhiêu bông hoa?",
            #"13. Mai có 10 nhãn vở, An có số nhãn vở gấp năm lần số nhãn vở của Mai. Hỏi cả hai bạn có tất cả bao nhiêu cái nhãn vở?",
            "14. Băng giấy đỏ dài 40 cm, băng giấy xanh dài hơn băng giấy đỏ 15 cm. Hỏi cả hai băng giấy dài bao nhiêu xăng-ti-mét?",
            "15. Một cửa hàng buổi sáng bán được 26 kg đường. Số đường buổi sáng bán được ít hơn số đường bán trong buổi chiều là 45 kg. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            "16. Một cửa hàng buổi sáng bán được 3 kg đường. Buổi chiều bán được số đường gấp hai lần số đường bán được vào buổi sáng. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            #"17. Ngăn trên có 14 quyển sách. Số quyển sách ở ngăn dưới bằng 1/2 số quyển ở ngăn trên. Hỏi cả hai ngăn có bao nhiêu quyển sách?",
            "18. Một cửa hàng buổi sáng bán được 52 kg đường. Số đường buổi sáng bán được nhiều hơn số đường bán trong buổi chiều 27 kg. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            #"19. Đàn gà có 40 gà trống, số gà mái bằng 1/8 số gà trống. Hỏi đàn gà có tất cả bao nhiêu con?",
            "20. Một cửa hàng buổi sáng bán được 24 kg đường. Buổi chiều bán được số đường bằng 1/6 số đường bán được vào buổi sáng. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            #"21. Đội đồng ca của lớp 1A có 36 nữ, số bạn nam ít hơn số bạn nữ là 32 em. Hỏi đội đồng ca của lớp 1A có bao nhiêu em?",
            "22. Mỹ hái được 5 bông hoa. Số bông hoa Linh hái được gấp sáu lần số hoa Mỹ hái được. Hỏi hai bạn hái được tất cả bao nhiêu bông hoa?",
            #"23. Mai có 9 nhãn vở, An có số nhãn vở gấp năm lần số nhãn vở của Mai. Hỏi cả hai bạn có tất cả bao nhiêu cái nhãn vở?",
            "24. Băng giấy xanh dài 11 cm, băng giấy đỏ dài hơn băng giấy xanh 2 cm. Hỏi cả hai băng giấy dài bao nhiêu xăng-ti-mét?",
            "25. Tổ một gấp được 28 cái thuyền, tổ hai gấp được gấp được nhiều hơn tổ một 11 cái thuyền. Hỏi cả hai tổ gấp được bao nhiêu cái thuyền?",
            "26. Một cửa hàng ngày thứ nhất bán được 34 lít dầu. Số dầu ngày thứ hai bán được bằng 1/2 số dầu bán được của ngày thứ nhất. Hỏi cả hai ngày cửa hàng bán được bao nhiêu lít dầu?",
            #"27. Ngăn trên có 32 quyển sách. Số quyển sách ở ngăn dưới bằng 1/4 số quyển ở ngăn trên. Hỏi cả hai ngăn có bao nhiêu quyển sách?",
            "28. Băng giấy đỏ dài 51 cm, băng giấy xanh ngắn hơn băng giấy đỏ 43 cm. Hỏi cả hai băng giấy dài bao nhiêu xăng-ti-mét?",
            #"29. Mai có 51 nhãn vở, An có số nhãn vở bằng 1/3 số nhãn vở của Mai. Hỏi cả hai bạn có tất cả bao nhiêu cái nhãn vở?",
            #"30. Đàn gà có 15 gà trống, số gà mái gấp bốn lần số gà trống. Hỏi đàn gà có tất cả bao nhiêu con?",
            "31. Mỹ hái được 12 bông hoa, Linh hái được nhiều hơn Mỹ 32 bông hoa. Hỏi hai bạn hái được tất cả bao nhiêu bông hoa?",
            "32. Một cửa hàng ngày thứ nhất bán được 30 lít dầu. Số dầu bán được của ngày thứ nhất ít hơn số dầu bán được của ngày thứ hai 21 lít. Hỏi cả hai ngày cửa hàng bán được bao nhiêu lít dầu?",
            #"33. Ngăn trên có 56 quyển sách. Số quyển sách ở ngăn dưới bằng 1/8 số quyển ở ngăn trên. Hỏi cả hai ngăn có bao nhiêu quyển sách?",
            "34. Ngăn trên có 36 quyển sách. Số sách ở ngăn trên ít hơn số sách ở ngăn dưới 20 quyển. Hỏi cả hai ngăn có bao nhiêu quyển sách?",
            "35. Một cửa hàng ngày thứ nhất bán được 68 lít dầu. Số dầu ngày thứ hai bán được bằng 1/4 số dầu bán được của ngày thứ nhất. Hỏi cả hai ngày cửa hàng bán được bao nhiêu lít dầu?"]

for i in test_str:
    engine = None
    engine = Engine(i)
    print(engine.res)
# engine = Engine(test_str[4])
# print(engine.res)
# for i in engine.OptSol:
#     print(i)
