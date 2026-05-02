import serial
import binascii
import time

def format_hex(data: bytes) -> str:
    hex_data = binascii.hexlify(data).decode('utf-8').upper()
    return ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))

def classify_packet(data: bytes) -> str:
    if len(data) < 5:
        return "Unknown"

    func_code = data[1]

    if func_code in [3, 4]:  # Read request
        if len(data) <= 8:
            return "Query"
        else:
            return "Response"
    elif func_code in [6, 16]:  # Write request
        return "Query" if len(data) <= 12 else "Response"
    else:
        return "Unknown"

def read_serial():
    try:
        ser = serial.Serial(port=port, baudrate=9600
            port=input("Enter COM port (e.g., COM4): "),
            baudrate = 9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1
        )
        print("Listening on", ser.portstr)

        while True:
            if ser.in_waiting:
                data = ser.read(ser.in_waiting)
                if data:
                    formatted = format_hex(data)
                    label = classify_packet(data)
                    timestamp = time.strftime("%H:%M:%S")
                    print(f"[{timestamp}] {label}: {formatted}")

    except serial.SerialException as e:
        print("Serial error:", e)
    except KeyboardInterrupt:
        print("\nStopped by user")

if __name__ == "__main__":
    read_serial()
