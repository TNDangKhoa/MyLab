from netmiko import ConnectHandler

def quick_ip_config_no_auth():
    print("\n=== CẤU HÌNH IP ===")
    
    target_host = input("1. Nhập IP quản lý (Fa0/0): ")

    # Cấu hình thiết bị chuyên dành cho Lab không bảo mật
    device = {
        'device_type': 'cisco_ios_telnet', # Telnet
        'host': target_host,
        'username': '',
        'password': '',
        'secret': '',
    }

    try:
        print(f"\nĐang kết nối tới {target_host} qua Telnet...")
        with ConnectHandler(**device) as net_connect:
            
            # Kiểm tra mode enable
            if not net_connect.check_enable_mode():
                net_connect.enable()

            while True: 
                print(f"\n--- Đang cấu hình các cổng cho Router {target_host} ---")
                int_name = input("  + Tên cổng cần đặt IP (VD: e1/0): ")
                ip_addr = input(f"  + Nhập IP cho {int_name}: ")
                mask_input = input("  + Nhập Subnet Mask (Default: 255.255.255.252): ")
                mask = mask_input if mask_input else "255.255.255.252"
             
                commands = [
                    f"interface {int_name}",
                    f"ip address {ip_addr} {mask}",
                    "ip ospf 1 area 0",
                    "mpls ip",
                    "no shutdown",
                    "exit"
                ]

                output = net_connect.send_config_set(commands)
                print("-" * 30)
                print(f"Kết quả cấu hình cổng {int_name}:")
                print(output)
                print("-" * 30)
                
                tiep_tuc_cong = input(f"Bạn có muốn cấu hình thêm cổng khác trên Router {target_host} không? (y/n): ")
                if tiep_tuc_cong.lower() != 'y':
                    break
            
            # --- CHỨC NĂNG KIỂM TRA NHANH SAU KHI XONG CÁC CỔNG ---
            print("\n>>> KIỂM TRA NHANH TRẠNG THÁI IP:")
            check_output = net_connect.send_command("show ip interface brief | exclude unassigned")
            print(check_output)
            
            net_connect.send_command("write memory")
            print(f"Đã lưu cấu hình cho {target_host} thành công!")
            
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    while True:
        quick_ip_config_no_auth()
        tiep_tuc = input("\nCấu hình tiếp sang ROUTER KHÁC? (y/n): ")
        if tiep_tuc.lower() != 'y':
            print("Đã thoát script.")
            break