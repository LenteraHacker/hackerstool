## HackersTool

clearscreen()
logo()
print("DW SQUAD OFFICAL")
Pilih menu:
  01) Create a Netcat Payload and Listener
  02) Facebook Group Hijack Attack
  03) SMS Bomber Attack Vectors
  04) SMS Spoof Attack Vectors
  05) Denial-of-Service Attack
  
  00) Exit the Tool
"""
santet = raw_input("santet > ")

if santet == "01" or santet == "1":
	netcat_rat()
elif santet == "02" or santet == "2":
	facebookgroup_hijack()
elif santet == "03" or santet == "3":
	sms_bomber_jdid()
elif santet == "04" or santet == "4":
	sms_spoof_elk()
elif santet == "05" or santet == "5":
	denialofservice_attack()
else:
	print "\nERROR: Wrong Input..."
	time.sleep(2)
	restart_program()
