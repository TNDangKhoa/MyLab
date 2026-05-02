#Tạo 1 robot barista

#khai báo biến
menu = "Cà phê đen - 10.000VND\n" + "Cà phê sữa - 12.000VND\n" + "Bạc xỉu - 15.000VND\n" + "Cà phê trứng - 18.000VND\n" + "Cà phê muối - 14.000VND\n"

#1. Chào hỏi khách hàng
print("Xin chào! Chào mừng bạn đến với quán cà phê của chúng tôi.")
name = input("Tên cảu bạn là gì?\n")
print("Rất vui được gặp bạn, " + name + "! Bạn muốn uống gì hôm nay?\n\n")
print("=" * 40 + "MENU" + "=" * 40)
print(menu)
print("=" * 85)

#2. Nhận đơn hàng
order = input("Vui lòng nhập tên đồ uống bạn muốn đặt: \n")
print("Bạn đã đặt: " + order)
print("Cảm ơn " + name + " đã đặt hàng, " + order + " của bạn sẽ được chuẩn bị trong giây lát.")

