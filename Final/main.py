# ==========================================================
# 1. ฟังก์ชันกระบวนการตรวจสอบและหักเงินใน Wallet
# ==========================================================
def process_payment(wallet_balance, item_price):
    # เงื่อนไข Wallet Balance ต้องมีค่ามากกว่าหรือเท่ากับราคาสินค้า
    if wallet_balance >= item_price:
        wallet_balance -= item_price  # หักยอดเงินสำเร็จ
        print(f"ชำระเงินสำเร็จ! ยอดเงินคงเหลือใหม่: {wallet_balance} บาท")
        return wallet_balance          # ส่งคืน Wallet Balance ใหม่
    else:
        print("Error: ยอดเงินใน Wallet ไม่เพียงพอสำหรับการชำระเงิน!")
        return wallet_balance          # ส่งคืน Wallet Balance เดิม


# ==========================================================
# 2. ฟังก์ชันวนลูปดึงข้อมูลคิวสั่งซื้อที่มี Status เป็น 'Pending'
# ==========================================================
def display_active_queues(queue_list):
    print("--- รายการคิวสั่งซื้อที่อยู่ระหว่างรอ (Pending) ---")
    
    # วนลูปเพื่อคัดกรองข้อมูลใน List ของคิวทั้งหมด
    for queue in queue_list:
        # ตรวจสอบว่าคิวสั่งซื้อมี Status เป็น 'Pending' หรือไม่
        if queue.get('Status') == 'Pending':
            print(f"คิวที่: {queue.get('Queue_ID')} | สินค้า: {queue.get('Item_Name')}")


# ==========================================================
# ส่วนทดสอบระบบ (Test Case)
# ==========================================================
if __name__ == "__main__":
    print("=== [ทดสอบฟังก์ชันที่ 1: process_payment] ===")
    current_wallet = 500
    print(f"ยอดเงินเริ่มต้นใน Wallet: {current_wallet} บาท\n")
    
    # รอบที่ 1: ซื้อของราคา 350 บาท (เงินพอ -> หักเงินสำเร็จ)
    print("-> พยายามซื้อสินค้าราคา 350 บาท")
    current_wallet = process_payment(current_wallet, 350) 
    print(f"ยอดเงินปัจจุบัน: {current_wallet} บาท\n")
    
    # รอบที่ 2: ซื้อของราคา 200 บาท (เงินไม่พอ เพราะเหลือแค่ 150 -> แสดง Error)
    print("-> พยายามซื้อสินค้าราคา 200 บาท")
    current_wallet = process_payment(current_wallet, 200) 
    print(f"ยอดเงินปัจจุบัน: {current_wallet} บาท\n")
    
    print("-" * 50)
    
    print("=== [ทดสอบฟังก์ชันที่ 2: display_active_queues] ===")
    # จำลองข้อมูล List ของคิวสั่งซื้อ (ใช้โครงสร้าง Dictionary)
    all_queues = [
        {'Queue_ID': 101, 'Item_Name': 'iPhone 15', 'Status': 'Pending'},
        {'Queue_ID': 102, 'Item_Name': 'iPad Air', 'Status': 'Completed'},
        {'Queue_ID': 103, 'Item_Name': 'MacBook Pro', 'Status': 'Pending'},
        {'Queue_ID': 104, 'Item_Name': 'AirPods', 'Status': 'Cancelled'}
    ]
    
    # เรียกใช้งานฟังก์ชันเพื่อแสดงผลเฉพาะคิวที่ Pending ออกทางหน้าจอ
    display_active_queues(all_queues)
